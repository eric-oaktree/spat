from django.shortcuts import render
from tracker.models import Tracker, Type, Scope
import time
from django.contrib.auth.models import User
from .forms import CDAForm, GartnerForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/users/login/')
def cda_req(request):
    if request.method != 'POST':
        date = time.strftime("%Y-%m-%d")
        bus = request.user
        pro = User.objects.get(username='oake')
        form = CDAForm(initial = {'start_date': date,
                                  'business_owner': bus,
                                  'proc_owner': pro})
    else:
        form = CDAForm(data=request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            type = Type.objects.get(type='CDA/NDA')
            scope = Scope.objects.get(scope='New')
            t.type = type
            t.scope = scope
            t.contract_value = 0
            t.theo = False
            t.status = 'Requested'
            t.save()

            return HttpResponseRedirect(reverse('tracker:index'))
    context = {'form': form}
    return render(request, 'reqs/cda_req.html', context)

@login_required(login_url='/users/login/')
def gartner_req(request):
    if request.method != 'POST':
        date = time.strftime("%Y-%m-%d")
        bus = request.user
        pro = User.objects.get(username='oake')
        form = GartnerForm(initial = {'start_date': date,
                                  'business_owner': bus,
                                  'proc_owner': pro})
    else:
        form = GartnerForm(data=request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            type = Type.objects.get(type='Research')
            scope = Scope.objects.get(scope='New')
            t.type = type
            t.scope = scope
            t.supplier = 'Gartner'
            t.contract_value = 0
            t.theo = False
            t.status = 'Requested'
            t.save()

            return HttpResponseRedirect(reverse('tracker:index'))
    context = {'form': form}
    return render(request, 'reqs/gartner_req.html', context)

def reqs(request):
    return render(request, 'reqs/reqs.html')

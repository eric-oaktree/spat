from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Tracker, Finance
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import TrackerForm, FinanceForm
import time
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = 0
    warning = 0
    warn = 0
    usr = 0
    if request.user.is_authenticated():
        rec = Tracker.objects.filter(proc_owner=request.user, end_date__isnull=True).order_by('start_date')
        rec_list = {}
        for r in rec:
            try:
                f = Finance.objects.get(record=r)
            except:
                f = 0
                warn = warn + 1
            rec_list[r] = f

        if warn > 1:
            warning = 'finance'

        proj = Tracker.objects.filter(business_owner=request.user, end_date__isnull=True).order_by('start_date')

        if request.user.groups.filter(name='Procurement Owners').exists():
            usr = 'Proc'

        context = {'rec':rec_list, 'proj':proj, 'warning': warning, 'usr': usr}
    return render(request, 'tracker/index.html', context)

def closed(request):
    context = 0
    usr = 0
    rec_list = {}
    if request.user.is_authenticated():
        rec = Tracker.objects.filter(proc_owner=request.user, end_date__isnull=False).order_by('-end_date')
        for r in rec:
            try:
                f = Finance.objects.get(record=r)
            except:
                f = 0
            rec_list[r] = f

        proj = Tracker.objects.filter(business_owner=request.user, end_date__isnull=False).order_by('-end_date')

        if request.user.groups.filter(name='Procurement Owners').exists():
            usr = 'Proc'

        context = {'rec':rec_list, 'proj':proj, 'usr': usr}
    return render(request, 'tracker/index.html', context)

def reqs(request):
    return render(request, 'tracker/reqs.html')

def detail(request, track_id):
    t = Tracker.objects.get(id=track_id)
    try:
        f = Finance.objects.get(record=t)
    except:
        f = 0
    if t.contract_value == 0:
        fin = 'd'
    else:
        fin = 'n'
    context = {'t':t, 'f':f, 'fin':fin}
    return render(request, 'tracker/detail.html', context)

def detailf(request, track_id):
    t = Tracker.objects.get(id=track_id)
    try:
        f = Finance.objects.get(record=t)
    except:
        f = 0
    context = {'t':t, 'f':f}
    return render(request, 'tracker/detailf.html', context)

@login_required(login_url='/users/login/')
def newtracker(request):
    if request.method != 'POST':
        date = time.strftime("%Y-%m-%d")
        u = request.user
        form = TrackerForm(initial = {'start_date': date, 'proc_owner': u})
    else:
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tracker:index'))
    context = {'form': form}
    return render(request, 'tracker/newtracker.html', context)

@login_required(login_url='/users/login/')
def newfinance(request, track_id):
    if request.method != 'POST':
        track = Tracker.objects.get(id=track_id)
        form = FinanceForm(initial={'record': track})
    else:
        form = FinanceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tracker:index'))
    context = {'form': form, 'track_id': track_id}
    return render(request, 'tracker/newfin.html', context)

@login_required(login_url='/users/login/')
def edittracker(request, track_id):
    if request.method != 'POST':
        track = Tracker.objects.get(id=track_id)
        form = TrackerForm(instance=track)
    else:
        track = Tracker.objects.get(id=track_id)
        form = TrackerForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tracker:detail', args=[track_id]))
    context = {'form' : form, 'track_id' : track_id}
    return render(request, 'tracker/edittracker.html', context)

@login_required(login_url='/users/login/')
def editfinance(request, fin_id):
    if request.method != 'POST':
        fin = Tracker.objects.get(id=fin_id)
        form = TrackerForm(instance=fin)
    else:
        fin = Tracker.objects.get(id=fin_id)
        form = TrackerForm(request.POST, instance=fin)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tracker:index'))
    context = {'form' : form, 'fin_id' : fin_id}
    return render(request, 'tracker/editfin.html', context)

@login_required(login_url='/users/login/')
def chk_del(request, track_id):
    t = Tracker.objects.get(id=track_id)
    context = {'t':t, 'track_id': track_id}
    return render(request, 'tracker/chk_del.html', context)

@login_required(login_url='/users/login/')
def delete(request, track_id):
    t = Tracker.objects.get(id=track_id)
    try:
        f = Finance.objects.get(record=t)
        f.delete()
    except:
        f = 0
    t.delete()
    return HttpResponseRedirect(reverse('tracker:index'))

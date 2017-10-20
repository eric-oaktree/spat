from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

from .models import Supplier, Publisher, Contact
from .forms import VendorForm, PublisherForm, ContactForm
from po.models import PO, Line_PO
from invoice.models import Invoice

def vendor_home(request):
    v = Supplier.objects.order_by('-viewed')
    v = v[:10]
    context = {'v': v}
    return render(request, 'vendor/vendor_home.html', context)

def vendor_detail(request, v_id):
    v = Supplier.objects.get(id=v_id)
    v.viewed = timezone.now()
    v.save()
    c = Contact.objects.filter(id=v_id)
    po = PO.objects.filter(supplier=v)
    context = {'v': v, 'c':c, 'po':po}
    return render(request, 'vendor/vendor_detail.html', context)

def contact_detail(request, c_id):
    c = Contact.objects.get(c_id)
    context = {'c':c}
    return render(request, 'vendor/contact_detail.html', context)

def add_vendor(request):
    if request.method == "POST":
        form = VendorForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            v = Supplier(name=data['name'], portal=data['portal'], desc=data['desc'])
            v.save()
            return HttpResponseRedirect(reverse('vendor:vendor_home'))
    else:
        form = VendorForm()
    context = {'form': form, 'mode': 'add'}
    return render(request, 'vendor/vendorform.html', context)

def edit_vendor(request, v_id):
    if request.method == "POST":
        form = VendorForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            v = Supplier.objects.get(id=v_id)
            v.name=data['name']
            v.portal=data['portal']
            v.desc=data['desc']
            v.modified = timezone.now()
            v.save()
            return HttpResponseRedirect(reverse('vendor:vendor_home'))
    else:
        v = Supplier.objects.get(id=v_id)
        form = VendorForm(initial = {'name': v.name, 'portal': v.portal, 'desc': v.desc})
    context = {'form': form, 'mode': 'edit', 'v_id': v_id}
    return render(request, 'vendor/vendorform.html', context)

def delete_vendor(request, v_id):
    v = Supplier.objects.get(id=v_id)
    v.delete()
    return HttpResponseRedirect(reverse('vendor:vendor_home'))

def del_check(request, v_id):
    v = Supplier.objects.get(id=v_id)
    context = {'ven': v, 'v_id': v_id}
    return render(request, 'vendor/del_check.html', context)

def add_contact(request, v_id):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            v = Supplier.objects.get(id=v_id)
            c = Contact(first=data['first'], last=data['last'], email=data['email'], phone=data['phone'], supplier=v)
            c.save()
            return HttpResponseRedirect(reverse('vendor:vendor_home'))
    else:
        form = ContactForm()
    context = {'form': form, 'mode': 'add', 'v_id': v_id}
    return render(request, 'vendor/contactform.html', context)

def edit_contact(request, c_id):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            c = Contact.objects.get(id=c_id)
            c.first = data['first']
            c.last = data['last']
            c.email = data['email']
            c.phone = data['phone']
            c.save()
            return HttpResponseRedirect(reverse('vendor:vendor_home' ))
    else:
        c = contact.objects.get(id=c_id)
        form = ContactForm(initial = {'first': c.first, 'last': c.last, 'supplier': c.supplier.name, 'email': c.email, 'phone': phone})
    context = {'form': form, 'mode': 'edit', 'c_id': c_id}
    return render(request, 'vendor/contactform.html', context)

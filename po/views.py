from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from .models import PO, Line_PO
from vendor.models import Supplier, Publisher
from .forms import POForm, LineForm

def po_home(request):
    pos = PO.objects.order_by('-viewed')
    pos = pos[:10]
    context = {'pos': pos}
    return render(request, 'po/po_home.html', context)

def po_detail(request, po_id):
    pos = PO.objects.get(id=po_id)
    lines = Line_PO.objects.filter(po=pos)
    subtotal = 0
    for ln in lines:
        subtotal = subtotal + ln.line_total
    pos.subtotal = subtotal
    try:
        pos.total = pos.tax_amt + subtotal
    except:
        pos.total = subtotal
    pos.save()
    context = {'pos': pos, 'lines':lines}
    return render(request, 'po/po_detail.html', context)

def add_po(request):
    pos = PO.objects.all().order_by('-num')
    try:
        last_po = pos[0]
        next_po = int(last_po.num) + 1
    except:
        next_po = 1
    if request.method == "POST":
        form = POForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            po = PO(
                #form fields
                supplier=data['supplier'], blanket=data['blanket'], auth=data['auth'], status=data['status'], comments=data['comments'], tax=data['tax'], tax_amt=data['tax_amt'], quote=data['quote'], budgeted=data['budgeted'],
                #auto fields
                num = next_po)
            po.save()
            return HttpResponseRedirect(reverse('po:po_home'))
    else:
        form = POForm()
    context = {'form': form, 'mode': 'add'}
    return render(request, 'po/poform.html', context)

def edit_po(request, po_id):
    if request.method == "POST":
        form = POForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            po= PO.objects.get(id=po_id)
            po.supplier = data['supplier']
            po.blanket = data['blanket']
            po.auth = data['auth']
            po.status = data['status']
            po.comments = data['comments']
            po.tax = data['tax']
            po.tax_amt = data['tax_amt']
            po.quote = data['quote']
            po.budgeted = data['budgeted']
            po.modified = timezone.now()
            po.save()
            return HttpResponseRedirect(reverse('po:po_detail', args=[po_id]))
    else:
        po = PO.objects.get(id=po_id)
        form = POForm(initial = {'supplier': po.supplier,
                                 'blanket': po.blanket,
                                 'auth': po.auth,
                                 'status': po.status,
                                 'comments': po.comments,
                                 'tax' : po.tax,
                                 'tax_amt' : po.tax_amt,
                                 'quote': po.quote,
                                 'budgeted': po.budgeted,
                                 })
    context = {'form': form, 'mode': 'edit', 'po_id': po_id}
    return render(request, 'po/poform.html', context)

def add_line(request, po_id):
    po = PO.objects.get(id=po_id)
    if request.method == "POST":
        form = LineForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ln = Line_PO(
            po=po, desc=data['desc'], item_num=data['item_num'],
            publisher=data['publisher'], quantity=data['quantity'],
            uom=data['uom'], unit_cost=data['unit_cost'],
            start_date=data['start_date'], exp_date=data['exp_date'],
            cost_center=data['cost_center'], budget_code=data['budget_code'],
            )
            ln.line_total = ln.quantity * ln.unit_cost
            ln.save()
            return HttpResponseRedirect(reverse('po:po_detail', args=[po_id]))
    else:
        form = LineForm(initial={'po': po})
    context = {'form': form, 'mode': 'add', "po_id": po_id}
    return render(request, 'po/lineform.html', context)

def edit_line(request, ln_id):
    ln = Line_PO.objects.get(id=ln_id)
    po = ln.po
    if request.method=="POST":
        form = LineForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ln.po=po
            ln.desc=data['desc']
            ln.publisher=data['publisher']
            ln.item_num=data['item_num']
            ln.quantity=data['quantity']
            ln.uom=data['uom']
            ln.unit_cost=data['unit_cost']
            ln.start_date=data['start_date']
            ln.exp_date=data['exp_date']
            ln.cost_center=data['cost_center']
            ln.budget_code=data['budget_code']
            ln.line_total = ln.quantity * ln.unit_cost
            ln.save()
            return HttpResponseRedirect(reverse('po:po_detail', args=[po.id]))
    else:
        ln = Line_PO.objects.get(id=ln_id)
        form = LineForm(initial={
                            'desc': ln.desc,
                            'item_num': ln.item_num,
                            'publisher': ln.publisher,
                            'quantity': ln.quantity,
                            'uom': ln.uom,
                            'unit_cost': ln.unit_cost,
                            'start_date': ln.start_date,
                            'exp_date': ln.exp_date,
                            'cost_center': ln.cost_center,
                            'budget_code': ln.budget_code,
        })

    context = {'form': form, 'mode': 'edit', 'po_id': po.id, "ln_id": ln_id}
    return render(request, 'po/lineform.html', context)

def po_by_vendor(request, v_id):
    v = Supplier.objects.get(id=v_id)
    pos = PO.objects.filter(supplier=v)
    context = {'v': v, 'pos': pos}
    return render(request, 'po/pobyvendor.html', context)

def add_po_to_vendor(request, v_id):
    v = Supplier.objects.get(id=v_id)
    pos = PO.objects.all().order_by('-num')
    try:
        last_po = pos[0]
        next_po = int(last_po.num) + 1
    except:
        next_po = 1
    if request.method == "POST":
        form = POForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            po = PO(
                #form fields
                supplier=data['supplier'], blanket=data['blanket'], auth=data['auth'], status=data['status'], comments=data['comments'], tax=data['tax'], tax_amt=data['tax_amt'], quote=data['quote'], budgeted=data['budgeted'],
                #auto fields
                num = next_po)
            po.save()
            return HttpResponseRedirect(reverse('po:po_home'))
    else:
        form = POForm(initial={'supplier': v})
    context = {'form': form, 'mode': 'add'}
    return render(request, 'po/poform.html', context)

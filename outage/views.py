from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import import_data

# Create your views here.
from .models import Environment, Service, Severity, Outage

def outage_detail(request):
    context = {}
    return render(request, 'outage/outage_detail.html', context)









def setup(request):
    prod_env = ('RMM', 'Continuity', 'HelpDesk', 'NOC', 'SOC')
    non_prod_env = ('Boston', 'Cranberry (non-HelpDesk)', 'Houston', 'Mumbai (non-NOC)', 'Pune (non-SOC)', 'London', 'Sydney')
    serv = ('Internet', 'Firewall', 'VPN', 'Wifi', 'Phones', 'Conference Room', 'VMware Engineering Environment', 'Applications')
    sev = (('Production Outage', 1), ('Production Degraded', 2), ('Non-Production Outage', 3), ('Non-Production Degraded', 4), ('Redundant Service Outage or Degregation', 5))
    e = Environment.objects.all()
    e.delete()
    s = Service.objects.all()
    s.delete()
    s = Severity.objects.all()
    s.delete()
    for x in prod_env:
        e = Environment(name=x, prod=True)
        e.save()
    for x in non_prod_env:
        e = Environment(name=x, prod=False)
        e.save()
    for x in serv:
        s = Service(name=x)
        s.save()
    for x in sev:
        s = Severity(name=x[0], value=int(x[1]))
        s.save()

    return HttpResponseRedirect(reverse('outage:dash'))

def load_x(request):
    de = Outage.objects.all()
    de.delete()
    d = import_data.d()
    for r in d:
        env = Environment.objects.get(name=r[1])
        serv = Service.objects.get(name=r[2])
        sev = Severity.objects.get(value=int(r[10]))
        o = Outage(description=r[0], environ=env, service=serv, sev=sev, began=r[3], detected=r[4], end=r[5]
                   , tz=r[6], owner=r[14], rca=r[15], status='Resolved')
        o.save()
    return HttpResponseRedirect(reverse('outage:dash'))

def dash(request):
    o = Outage.objects.all()
    context = {'outage': o}
    return render(request, 'outage/dash.html', context)

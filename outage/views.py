from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from .models import Environment, Service, Severity, Outage

def setup(request):
    prod_env = ('RMM', 'Continuity', 'HelpDesk', 'NOC', 'SOC')
    non_prod_env = ('Boston', 'Cranberry (non-HelpDesk)', 'Houston', 'Mumbai (non-NOC)', 'Pune (non-SOC)', 'London', 'Sydney')
    serv = ('Internet', 'Firewall', 'VPN', 'Wifi', 'Phones', 'Conference Room', 'VMware Engineering Environment', 'Applications')
    sev = (('Production Outage', 1), ('Production Degraded', 2), ('Non-Production Outage', 3), ('Non-Production Degraded', 4), ('Redundant Service Outage or Degregation', 5))

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
        s = Severity(name=x[0], value=x[1])

    return HttpResponseRedirect(render('outage:dash'))

def dash(request):
    o = Outage.objects.all()
    context = {'outage': o}
    return render(request, 'outage/dash.html')

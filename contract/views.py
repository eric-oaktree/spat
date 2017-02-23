from django.shortcuts import render
from .models import Contract

# Create your views here.

def recent_con(request):
    cons = Contract.objects.all().order_by('-viewed')
#    i = 0
#    con_dict = {}
#    b = []
    con = cons[0:19]
#    while i <= 20:
#        con = cons[i]
#        name = con.name
#        eff = con.eff_date
#        sup = con.supplier
#        a = (name, eff, sup)
#
#        i = i++
    context = {'con': con}
    return render(request, 'contract/list.html', context)

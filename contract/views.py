from django.shortcuts import render
from .models import Contract

# Create your views here.

def recent_con(request):
    cons = Contract.objects.all().order_by('-viewed')
    con = cons[0:19]
    context = {'con': con}
    return render(request, 'contract/list.html', context)

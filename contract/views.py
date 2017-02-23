from django.shortcuts import render
from .models import Contract

# Create your views here.

def list(request):
    cons = Contract.objects.all()
    return render(request, 'contract/list.html')

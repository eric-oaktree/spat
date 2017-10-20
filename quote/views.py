from django.shortcuts import render

# Create your views here.

from .models import Project, Quote, Line_quo

def quotes_home(request):
    q = Quote.objects.order_by('-created')
    q = q[:10]
    context = {'q':q}
    return render(request, 'quote/quotes_home.html')

def quotes_detail(request, q_id):
    q = Quote.objects.get(id=q_id)
    l = Line_quo.objects.filter(quote=q_id)
    context = {'q': q, 'l': l}
    return render(request, 'quote/quotes_detail.html', context)



def project_home(request):
    p = Project.objects.order_by('-created')
    p = p[:10]
    context = {'p': p}
    return render(request, 'quote/project_home.html', context)

def project_detail(request, p_id):
    p = Project.objects.get(id=p_id)
    q = Quote.objects.filter(project=p_id)
    context = {'p': p, 'q': q}
    return render(request, 'quote/prodject_detail.html', context)

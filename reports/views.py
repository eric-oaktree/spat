from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from tracker.models import Tracker, Finance
from django.core.urlresolvers import reverse

# Create your views here.

def home(request):
    return render(request, 'reports/home.html')


def at_csv_dump(request):
    track = Tracker.objects.all()
    csv_dump = open('csv_dump.csv', 'w')
    csv_dump.write('Initiative Name,Supplier,Type,Scope,Comments,StartDate,EndDate,BusinessOwner,SBU,ProcOwner,Category\n')
    for t in track:
        csv_dump.write(t.init_name+','+t.supplier+','+t.type.type+','+t.scope.scope+','+t.comments+','+str(t.start_date)+','+str(t.end_date)+','+t.business_owner.first_name+t.business_owner.last_name+','+t.division.division+','+t.proc_owner.first_name+t.proc_owner.last_name+','+t.category.category+'\n')
    csv_dump.close()
    csv_dump = open('csv_dump.csv', 'r')
    response = HttpResponse(csv_dump, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="at_csv_dump.csv"'
    return response

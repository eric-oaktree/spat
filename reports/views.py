from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from tracker.models import Tracker, Finance
from django.core.urlresolvers import reverse
from datetime import datetime, date
from reports.models import Historical


# Create your views here.

def home(request):
    #grab all data
    data = Tracker.objects.all()
    #grab data filed to open items
    open = Tracker.objects.filter(end_date__isnull=True)
    acount = 0.0
    asum = 0.0
    cat_sum_dict = {}
    cat_count_dict = {}
    #run through open items and calculate averages
    for t in open:
        ed = date.today()
        sd = t.start_date
        day  = ed - sd
        acount = acount + 1
        asum = asum + day.days
        #make sure the key exists in the dictionary
        if t.type in cat_sum_dict:
            a = 1 + 1
        else:
            cat_sum_dict[t.type] = 0.0
        #make sure the key exists in the dictionary
        if t.type in cat_count_dict:
            b = 1 + 1
        else:
            cat_count_dict[t.type] = 0.0
        #write the intances data to the dictionary
        cat_sum_dict[t.type] = cat_sum_dict[t.type] + day.days
        cat_count_dict[t.type] = cat_count_dict[t.type] + 1
    #cacluate all average
    all_average = asum / acount

    #calcualte avg by category
    cat_avg = {}
    for cat in cat_sum_dict.keys():
        avg = cat_sum_dict[cat] / cat_count_dict[cat]
        cat_avg[cat] = avg

    context = {'data': data, 'all_average': all_average, 'cat_avg': cat_avg}
    return render(request, 'reports/home.html', context)


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

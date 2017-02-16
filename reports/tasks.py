# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from tracker.models import Tracker, Finance
from reports.models import Historical
from django.core.urlresolvers import reverse
from datetime import datetime, date


@shared_task
def rec_days_out():
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
    #write to DB
    r = Historical(key='all_open', value=all_average)

    #calcualte avg by category
    cat_avg = {}
    for cat in cat_sum_dict.keys():
        avg = cat_sum_dict[cat] / cat_count_dict[cat]
        cat_avg[cat] = avg
        rc = Historical(key=cat, value=avg)

    

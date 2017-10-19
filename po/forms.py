from django import forms

from .models import PO, Line_PO, Cost_Center
from vendor.models import Supplier, Publisher
from quote.models import Quote
from django.contrib.auth.models import User


class POForm(forms.Form):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())
    blanket = forms.BooleanField(required=False)
    auth = forms.ModelChoiceField(queryset=User.objects.all())
    status = forms.CharField(strip=True) #make this a dropdown?
    comments = forms.CharField(strip=True, required=False)
    #add tax handling
    tax = forms.BooleanField(required=False)
    tax_amt = forms.DecimalField(max_digits=5, decimal_places=5, required=False)
    quote = forms.ModelChoiceField(queryset=Quote.objects.all(), required=False)
    budgeted = forms.BooleanField()

class LineForm(forms.Form):
    desc = forms.CharField(strip=True)
    item_num = forms.CharField(strip=True, required=False)
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all(), required=False)
    quantity = forms.IntegerField()
    uom = forms.CharField(strip=True)
    unit_cost = forms.DecimalField(max_digits=19, decimal_places=2)
    start_date = forms.DateField(required=False)
    exp_date = forms.DateField(required=False)
    cost_center = forms.ModelChoiceField(queryset=Cost_Center.objects.all(), required=False)
    budget_code = forms.DecimalField(max_digits=6, decimal_places=3, required=False)

class CostCenterForm(forms.Form):
    pass


#cost_center = forms.ModelChoiceField(queryset=Cost_Center.objects.all())

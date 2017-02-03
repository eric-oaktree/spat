from django import forms

from tracker.models import Tracker

class CDAForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['init_name', 'supplier', 'comments', 'start_date', 'business_owner', 'division', 'proc_owner', 'category']
        labels = {'init_name': 'Initiative Name', 'supplier': 'Supplier Name', 'comments': 'Comments', 'start_date': 'Activity Start Date (YYYY-MM-DD)', 'business_owner': 'Business Owner', 'division': 'SBU', 'proc_owner': 'Procurement Owner', 'category': 'Category'}

class GartnerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['init_name', 'comments', 'start_date', 'business_owner', 'division', 'proc_owner', 'category']
        labels = {'init_name': 'Initiative Name', 'comments': 'Comments', 'start_date': 'Activity Start Date (YYYY-MM-DD)', 'business_owner': 'Business Owner', 'division': 'SBU', 'proc_owner': 'Procurement Owner', 'category': 'Category'}

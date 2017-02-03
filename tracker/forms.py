from django import forms

from .models import Tracker, Finance

class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['init_name', 'supplier', 'type', 'scope', 'comments', 'theo', 'start_date', 'end_date', 'business_owner', 'division', 'proc_owner', 'category', 'contract_value', 'status']
        labels = {'init_name': 'Initiative Name', 'supplier': 'Supplier Name', 'type': 'Activity Type', 'scope': 'Activity Scope',
                  'comments': 'Comments', 'theo': 'Planned Project?', 'start_date': 'Activity Start Date (YYYY-MM-DD)', 'end_date': 'Activity End Date (YYYY-MM-DD)',
                  'business_owner': 'Business Owner', 'division': 'SBU', 'proc_owner': 'Procurement Owner', 'category': 'Category', 'contract_value': 'Total Contract Value', 'status': 'Status' }

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['record','term_mo', 'yr_savings', 'spend_cur_fy', 'spend_prev_fy', 'contract_start', 'contract_end',
                  'savings_start', 'savings_end', 'budget_type', 'cs_type', 'confidence', 'nature']
        labels = {'record': 'Tracker', 'term_mo': 'Term in Months', 'yr_savings': '12 mo Savings', 'spend_cur_fy': 'Current FY Spend', 'spend_prev_fy': 'Previous FY Spend', 'contract_start': 'Contract Start Date (YYYY-MM-DD)', 'contract_end': 'Contract End Date (YYYY-MM-DD)',
                  'savings_start': 'Savings Start Date (YYYY-MM-DD)', 'savings_end': 'Savings End Date (YYYY-MM-DD)', 'budget_type': 'Budget Type', 'cs_type': 'Cost Savings Type', 'confidence': 'Confidence Level', 'nature': 'Nature of Deal'}

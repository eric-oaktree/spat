from django import forms

from .models import Outage

class OutageForm(forms.ModelForm):
    class Meta:
        model = Outage
        fields = ['description', 'environ', 'service', 'sev', 'began', 'detected', 'end', 'tz', 'auth_owner', 'rca', 'status']
        labels = {'description': 'Name of Outage', 'environ': 'Environment', 'service': 'Service Affected',
                    'sev': 'Severity', 'began': 'Time Outage Began', 'detected': 'Time Outage Was Detected', 'end': 'Time Outage Ended',
                    'tz': 'Timezone (XXX)', 'owner': 'Resolution Owner', 'rca': 'Root Cause Analysis', 'status': 'Outage Status'}

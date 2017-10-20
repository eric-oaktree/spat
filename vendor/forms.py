from django import forms

from .models import Supplier, Publisher, Contact

class VendorForm(forms.Form):
    name = forms.CharField(strip=True)
    portal = forms.URLField()
    desc = forms.CharField(strip=True)

class PublisherForm(forms.Form):
    product = forms.CharField(strip=True)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())
    alt_supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())

class ContactForm(forms.Form):
    first = forms.CharField(strip=True)
    last = forms.CharField(strip=True)
    email = forms.EmailField()
    phone = forms.CharField(strip=True)

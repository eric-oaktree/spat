from django.contrib import admin

# Register your models here.

from .models import Contact, Supplier, Contract, Note

admin.site.register(Contact)
admin.site.register(Supplier)
admin.site.register(Contract)
admin.site.register(Note)

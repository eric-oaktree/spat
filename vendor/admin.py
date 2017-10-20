from django.contrib import admin

# Register your models here.

from .models import Supplier, Publisher, Contact

admin.site.register(Supplier)
admin.site.register(Publisher)
admin.site.register(Contact)

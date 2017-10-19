from django.contrib import admin

from .models import PO, Line_PO, Cost_Center

# Register your models here.

admin.site.register(PO)
admin.site.register(Cost_Center)
admin.site.register(Line_PO)

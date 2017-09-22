from django.contrib import admin

# Register your models here.
from .models import Environment, Service, Severity, Outage

admin.site.register(Environment)
admin.site.register(Service)
admin.site.register(Severity)
admin.site.register(Outage)

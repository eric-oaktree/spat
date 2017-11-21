from django.contrib import admin

# Register your models here.

from .models import Category, SBU, Scope, Type, Tracker, Finance, Budget, CSType, Confidence, TaskStatus, Task

admin.site.register(Category)
admin.site.register(SBU)
admin.site.register(Scope)
admin.site.register(Type)
admin.site.register(Tracker)
admin.site.register(Finance)
admin.site.register(Budget)
admin.site.register(CSType)
admin.site.register(Confidence)
admin.site.register(TaskStatus)
admin.site.register(Task)

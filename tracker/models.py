from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class SBU(models.Model):
    division = models.CharField(max_length=50)
    def __str__(self):
        return self.division

class Scope(models.Model):
    scope = models.CharField(max_length=50)
    def __str__(self):
        return self.scope

class Type(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.type

class Tracker(models.Model):
    init_name = models.CharField(max_length=50)
    supplier = models.CharField(max_length=50)
    type  = models.ForeignKey(Type)
    scope  = models.ForeignKey(Scope)
    comments = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    business_owner = models.ForeignKey(User, related_name='bus')
    division = models.ForeignKey(SBU)
    proc_owner = models.ForeignKey(User, related_name='proc', limit_choices_to={'groups':1})
    category = models.ForeignKey(Category)
    contract_value = models.DecimalField(max_digits=10, decimal_places=2)
    theo = models.BooleanField(default=False)
    status = models.CharField(max_length=140)
    def __str__(self):
        return self.init_name

class Budget(models.Model):
    budget_type = models.CharField(max_length=50)
    def __str__(self):
        return self.budget_type

class CSType(models.Model):
    cs_type = models.CharField(max_length=50)
    def __str__(self):
        return self.cs_type

class Confidence(models.Model):
    confidence = models.CharField(max_length=50)
    def __str__(self):
        return self.confidence

class Finance(models.Model):
    record = models.ForeignKey(Tracker)
    term_mo = models.IntegerField()
    yr_savings = models.DecimalField(max_digits=10, decimal_places=2)
    spend_cur_fy = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    spend_prev_fy = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contract_start = models.DateField()
    contract_end = models.DateField(null=True, blank=True)
    savings_start = models.DateField(null=True, blank=True)
    savings_end = models.DateField(null=True, blank=True)
    budget_type = models.ForeignKey(Budget, null=True, blank=True)
    cs_type = models.ForeignKey(CSType, null=True, blank=True)
    confidence = models.ForeignKey(Confidence, null=True, blank=True)
    nature = models.TextField()
    def __str__(self):
        return str(self.record) + ' ' + str(self.contract_start)

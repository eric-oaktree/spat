from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

from vendor.models import Supplier, Publisher

class Project(models.Model):
    name = models.TextField()
    desc = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return self.name

class Quote(models.Model):
    desc = models.TextField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier)
    quote_num = models.TextField()
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True)
    tax = models.BooleanField()
    tax_amt = models.DecimalField(max_digits=5, decimal_places=5)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    total = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    def __str__(self):
        return str(self.supplier.name)+"-"+str(self.quote_num)

class Line_quo(models.Model):
    quote = models.ForeignKey(Quote)
    desc = models.TextField()
    item_num = models.TextField(null=True, blank=True)
    publisher = models.ForeignKey(Publisher, models.SET_NULL, blank=True, null=True)
    qty = models.DecimalField(max_digits=19, decimal_places=10)
    uom = models.TextField()
    unit_cost = models.DecimalField(max_digits=19, decimal_places=10)
    start_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    line_total = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    def __str__(self):
        return str(self.desc)

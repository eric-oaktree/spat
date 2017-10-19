from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.

from vendor.models import Supplier, Publisher
from quote.models import Quote

class Cost_Center(models.Model):
    name = models.CharField(max_length=140)
    owner = models.ForeignKey(User, models.SET_NULL, null=True)
    dept_code = models.IntegerField(null=True)
    def __str__(self):
        return self.name


class PO(models.Model):
    supplier = models.ForeignKey(Supplier, models.SET_NULL, null=True)
    num = models.IntegerField(unique=True)
    issued = models.DateTimeField(null=True, blank=True)
    blanket = models.BooleanField(default=False)
    auth = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    status = models.TextField() #make this a dropdown?
    comments = models.TextField(null=True, blank=True)
    #add tax handling
    tax = models.BooleanField(default=False)
    tax_amt = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    quote = models.ForeignKey(Quote, models.SET_NULL, null=True, blank=True)
    budgeted = models.BooleanField(default=False)
    version = models.IntegerField(default=1)
    def __str__(self):
        return str(self.supplier.name)+str(self.num)

class Line_PO(models.Model):
    po = models.ForeignKey(PO)
    desc = models.TextField()
    item_num = models.TextField(null=True, blank=True)
    publisher = models.ForeignKey(Publisher, models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    uom = models.TextField()
    unit_cost = models.DecimalField(max_digits=19, decimal_places=2)
    dept_code = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField(null=True, blank=True)
    cost_center = models.ForeignKey(Cost_Center, models.SET_NULL, null=True, blank=True)
    budget_code = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    line_total = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    def __str__(self):
        return str(self.desc)

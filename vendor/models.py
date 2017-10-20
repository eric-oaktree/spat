from django.db import models
from django.utils import timezone
# Create your models here.

class Supplier(models.Model):
    name = models.TextField(unique=True)
    portal = models.URLField(null=True)
    desc = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return str(self.name)

class Publisher(models.Model):
    product = models.TextField
    supplier = models.ForeignKey(Supplier, related_name='pubs')
    alt_supplier = models.ForeignKey(Supplier, models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return str(self.product)

class Contact(models.Model):
    first = models.TextField()
    last =  models.TextField()
    supplier = models.ForeignKey(Supplier, related_name='cont')
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    viewed = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return str(self.first)+str(self.last)

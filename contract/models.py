from django.db import models

# Create your models here.

class Contact(models.Model):
    first = models.CharField(max_length=140)
    last = models.CharField(max_length=140)
    email = models.EmailField(max_length=254, blank=True)
    number = models.IntegerField()
    def __str__(self):
        return self.first + ' ' + self.last

class Supplier(models.Model):
    name = models.CharField(max_length=140)
    main_contact = models.ForeignKey(Contact)
    def __str__(self):
        return self.name

class Contract(models.Model):
    name = models.CharField(max_length=140)
    def __str__(self):
        return self.name

class Note(models.Model):
    note = models.TextField()
    supplier = models.ForeignKey(Supplier)
    def __str__(self):
        return self.note

from django.db import models

# Create your models here.

class Contact(models.Model):
    first = models.CharField(max_length=140)
    last = models.CharField(max_length=140)
    email = models.EmailField(max_length=254, blank=True)
    number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()
    viewed = models.DateTimeField()

    def __str__(self):
        return self.first + ' ' + self.last

class Supplier(models.Model):
    name = models.CharField(max_length=140)
    main_contact = models.ForeignKey(Contact)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()
    viewed = models.DateTimeField()
    def __str__(self):
        return self.name

class Contract(models.Model):
    name = models.CharField(max_length=140)
    eff_date = models.DateField()
    end_date = models.DateField()
    perp = models.NullBooleanField()
    term_note = models.IntegerField()
    auto_renew = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()
    viewed = models.DateTimeField()
    def __str__(self):
        return self.name

class Note(models.Model):
    note = models.TextField()
    supplier = models.ForeignKey(Supplier)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()
    viewed = models.DateTimeField()
    def __str__(self):
        return self.note

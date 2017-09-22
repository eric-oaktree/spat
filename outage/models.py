from django.db import models

# Create your models here.

class Environment(models.Model):
    name = models.TextField()
    prod = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Severity(models.Model):
    name = models.TextField()
    value = models.IntegerField()
    def __str__(self):
        return self.name

class Outage(models.Model):
    description = models.TextField(null=True)
    environ = models.ForeignKey(Environment)
    service = models.ForeignKey(Service)
    sev = models.ForeignKey(Severity)
    began = models.DateTimeField(null=True)
    detected = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    tz = models.CharField(max_length=3)
    owner = models.TextField(null=True)
    rca = models.TextField(null=True)
    status = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.description

from django.db import models

# Create your models here.

class Historical(models.Model):
    date = models.DateField(auto_now_add=True)
    key = models.CharField(max_length=140)
    value = models.DecimalField(max_digits=19, decimal_places = 5)
    def  __str__(self):
        return str(self.key) + str(self.date)

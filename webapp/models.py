from django.db import models
from django.urls import reverse

# Create your models here.

class Items(models.Model):
    item_name=models.CharField(max_length=250)
    item_quantity=models.CharField(max_length=250)
    item_status=models.IntegerField()
    date=models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('appweb:homepage')

    def __str__(self):
        return self.item_name

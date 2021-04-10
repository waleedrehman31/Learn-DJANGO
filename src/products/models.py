from django.db import models
from django.urls import reverse

# Create your models here.


class Product (models.Model):
    title = models.CharField(max_length=120)  # max_length = require
    discription = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField()
    featured = models.BooleanField(default=True)  # null = ture, default = True


# pylint: disable=E1101


    def get_absolute_url(self):
        # f"/products/{self.id}/"
        return reverse("products:product-detail", kwargs={"id": self.id})


''' 
If blank = false means field is required and if null = false means database needs some data
blank deals with user
null deals with database i.e sqlite
'''

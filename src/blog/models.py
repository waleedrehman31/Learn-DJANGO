from django.db import models
from django.urls import reverse

# Create your models here.


class Article (models.Model):
    title = models.CharField(max_length=120)  # max_length = require
    content = models.TextField()
    active = models.BooleanField(default=True)
# pylint: disable=E1101

    def get_absolute_url(self):
        return reverse("articles:Article-detail", kwargs={"id": self.id})

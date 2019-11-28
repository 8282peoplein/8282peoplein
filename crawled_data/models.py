from django.db import models

# Create your models here.
from django.urls import reverse


class BoardData(models.Model):
    title = models.CharField(max_length=300)
    link = models.URLField()
    specific_id = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class BlogData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
    	return self.title





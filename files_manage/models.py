from django.db import models
from django import forms
# Create your models here.
class fileModel(models.Model):
    file = models.FileField(upload_to='upload')
    path = models.CharField(max_length=255)
    upload_date = models.DateField(auto_now_add=True)
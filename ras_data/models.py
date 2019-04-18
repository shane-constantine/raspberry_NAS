from django.db import models

# Create your models here.
class ras_info(models.Model):
    T = models.FloatField(max_length=255,default=0)
    H = models.FloatField(max_length=255,default=0)
    CT = models.FloatField(max_length=255,default=0)
    CU = models.FloatField(max_length=255,default=0)
    DT = models.FloatField(max_length=255, default=0)
    DU = models.FloatField(max_length=255, default=0)
    DF = models.FloatField(max_length=255, default=0)
    DP = models.FloatField(max_length=255, default=0)
    RT = models.FloatField(max_length=255, default=0)
    RU = models.FloatField(max_length=255, default=0)
    RF = models.FloatField(max_length=255, default=0)
    RP = models.FloatField(max_length=255, default=0)
    upload_date = models.DateField(auto_now_add=True)

from django.db import models

# Create your models here.
class val(models.Model):
    v1=models.IntegerField()
    v2 = models.IntegerField()
    v3=models.CharField(max_length=10,default=0)
class Cron(models.Model):
    name=models.CharField(max_length=10)
    days=models.IntegerField(choices=[(x, x) for x in range(1, 32)])
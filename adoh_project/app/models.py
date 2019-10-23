from django.db import models

# Create your models here.
class student(models.Model):
    sb1=models.IntegerField()
    sb2=models.IntegerField()
    sb3=models.IntegerField(default=0)
    total=models.CharField(max_length=20)




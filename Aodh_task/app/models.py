from django.db import models

# Create your models here.
class helth(models.Model):
    heartbeat=models.IntegerField()
    himoglobin=models.IntegerField()
    breathingrate=models.IntegerField()

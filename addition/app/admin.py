from django.contrib import admin

# Register your models here.
from app.models import val,Cron
admin.site.register(val)
admin.site.register(Cron)
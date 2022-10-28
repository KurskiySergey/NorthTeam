from django.db import models
# Create your models here.


class TG_User(models.Model):
    tg_id = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    username = models.CharField(blank=True, null=True, max_length=255)
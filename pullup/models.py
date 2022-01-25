from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class customer(models.Model):
    member_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=50, null=True)
    member_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)

    class Meta:
        db_table = 'customer'
        app_label = 'pullup'
        managed = False
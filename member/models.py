from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Member(models.Model):
    member_id = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50, null=True)
    member_name = models.CharField(max_length=50, null=True)
    psw_rg = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)

    class Meta:
        db_table = 'member'
        app_label = 'member'
        managed = True
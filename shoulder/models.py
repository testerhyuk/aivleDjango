from django.db import models
from django.db.models.fields import IntegerField

class Shoulder(models.Model):
    cnt = models.IntegerField()
    
    class Meta:
        db_table = "shoulder_cnt"
        managed = False
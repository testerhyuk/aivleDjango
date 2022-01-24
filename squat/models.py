from django.db import models

class Squat(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.DateField()
    cnt = models.IntegerField()
    time = models.TimeField()
    
    class Meta:
        db_table = "train_data"
        managed = False

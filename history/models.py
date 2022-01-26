from django.db import models

# Create your models here.
class History(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    triceps = models.IntegerField(null=True)
    shoulder = models.IntegerField(null=True)
    squat = models.IntegerField(null=True)
    pullup = models.IntegerField(null=True)
    vrksasana = models.IntegerField(null=True)

    class Meta:
        db_table = 'history'
        app_label = 'history'
        managed = True
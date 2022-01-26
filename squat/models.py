from django.db import models
from django.db.models.fields import IntegerField, DateField

class Squat(models.Model):
    exercise_date = DateField()
    count = IntegerField()
    # member_id = models.OneToOneField(Member, on_delete=models.CASCADE, null=True

    class Meta:
        db_table = "squat"
        managed = False

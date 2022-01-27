from django.db import models
from member.models import Member

# Create your models here.
class History(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
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


class Profile(models.Model):
    image = models.ImageField(upload_to='profile/', null=True)
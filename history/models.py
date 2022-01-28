from django.db import models
from member.models import Member

# Create your models here.
class History(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=True)
    triceps = models.IntegerField(default=0)
    shoulder = models.IntegerField(default=0)
    squat = models.IntegerField(default=0)
    pullup = models.IntegerField(default=0)
    vrksasana = models.IntegerField(default=0)

    class Meta:
        db_table = 'history'
        app_label = 'history'
        managed = True


class Profile(models.Model):
    file = models.FileField(upload_to='profile/', null=True)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
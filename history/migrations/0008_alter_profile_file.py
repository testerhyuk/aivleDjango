# Generated by Django 3.2.11 on 2022-01-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0007_profile_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file',
            field=models.FileField(default='static/assets/img/profile/profile_default.jpg', null=True, upload_to='profile/'),
        ),
    ]

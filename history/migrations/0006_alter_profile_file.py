# Generated by Django 3.2.11 on 2022-01-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0005_auto_20220127_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file',
            field=models.FileField(null=True, upload_to='profile/'),
        ),
    ]

# Generated by Django 3.2.11 on 2022-01-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0008_alter_profile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='file',
            field=models.FileField(default='settings.MEDIA_ROOT/default/profile_default.jpg', null=True, upload_to='profile/'),
        ),
    ]

# Generated by Django 3.2.11 on 2022-01-27 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('history', '0006_alter_profile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.member'),
        ),
    ]
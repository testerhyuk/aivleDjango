# Generated by Django 3.2.11 on 2022-01-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='name',
            new_name='member_id',
        ),
    ]

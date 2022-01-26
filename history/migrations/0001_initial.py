# Generated by Django 3.2.11 on 2022-01-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('triceps', models.IntegerField(null=True)),
                ('shoulder', models.IntegerField(null=True)),
                ('squat', models.IntegerField(null=True)),
                ('pullup', models.IntegerField(null=True)),
                ('vrksasana', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'history',
                'managed': True,
            },
        ),
    ]
<<<<<<< HEAD
# Generated by Django 4.0.1 on 2022-01-30 17:54

from django.db import migrations, models
=======
# Generated by Django 3.2.5 on 2022-01-28 14:31

from django.db import migrations, models
import django.db.models.deletion
>>>>>>> 0adef8e15f6794fc6c8c3d907892b3a049df42f8


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
=======
        ('member', '0001_initial'),
>>>>>>> 0adef8e15f6794fc6c8c3d907892b3a049df42f8
        ('history', '0013_alter_history_pullup_alter_history_shoulder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
<<<<<<< HEAD
                ('member_id', models.CharField(max_length=50, unique=True)),
                ('total', models.IntegerField()),
            ],
            options={
                'managed': False,
=======
                ('total', models.IntegerField()),
                ('member_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.member')),
            ],
            options={
                'managed': True,
>>>>>>> 0adef8e15f6794fc6c8c3d907892b3a049df42f8
            },
        ),
    ]

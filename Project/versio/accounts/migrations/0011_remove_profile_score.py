# Generated by Django 2.2.1 on 2019-05-11 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='score',
        ),
    ]

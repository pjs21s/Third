# Generated by Django 2.1.7 on 2019-04-13 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190413_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(),
        ),
    ]

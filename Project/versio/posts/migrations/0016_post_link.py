# Generated by Django 2.1.7 on 2019-04-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20190420_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='', max_length=100),
        ),
    ]

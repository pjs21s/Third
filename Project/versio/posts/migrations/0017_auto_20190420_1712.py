# Generated by Django 2.1.7 on 2019-04-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(),
        ),
    ]
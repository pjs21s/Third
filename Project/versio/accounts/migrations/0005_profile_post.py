# Generated by Django 2.1.7 on 2019-05-06 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_auto_20190502_1745'),
        ('accounts', '0004_profile_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]
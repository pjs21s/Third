# Generated by Django 2.1.7 on 2019-05-06 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.Post'),
        ),
    ]
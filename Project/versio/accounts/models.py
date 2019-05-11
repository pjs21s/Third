from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=300, blank=True)
    lang = models.CharField(max_length=20, blank=True)
    logined_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse(
            "accounts:profile",
            kwargs={
                "pk": self.pk
            }
        )

def login_user(sender, request, user, **kwargs):
    user.profile.logined_count = user.profile.logined_count + 1
    user.profile.save()

user_logged_in.connect(login_user)

@receiver(post_save, sender=auth.models.User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=auth.models.User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


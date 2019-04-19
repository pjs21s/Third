from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin
# Create your models here.

class Post(models.Model, HitCountMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    text = RichTextField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["title"]
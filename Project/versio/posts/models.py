from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin
from django.conf import settings
from tagging.fields import TagField

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ["category_name"]
    
    def __str__(self):
        return self.category_name

class Post(models.Model, HitCountMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now=True)
    text = RichTextUploadingField()
    title = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    tag = TagField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        blank=True,
                                        related_name='like_user_set',
                                        through='Like')

    def __str__(self):
        return self.title

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

    @property
    def like_count(self):
        return self.like_user_set.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_date = models.DateTimeField(auto_now=True)
    comment_text = models.CharField(max_length=200)
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.comment_text

    class Meta:
        ordering = ["comment_date"]

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
       fields = ("title", "text")
       model = models.Post
    
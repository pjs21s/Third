from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
       fields = ("title","link", "text", )
       model = models.Post
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('comment_text',)
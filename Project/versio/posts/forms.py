from django.forms import ModelForm
from . import models

class PostForm(ModelForm):
    class Meta:
       fields = ("title","category", "link", "text", "tag")
       model = models.Post
    
class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ('comment_text',)
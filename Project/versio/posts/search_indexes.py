import datetime
from haystack import indexes
from .models import Post


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='search/post_text.txt')
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='created_at')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

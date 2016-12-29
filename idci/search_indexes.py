from django.utils import timezone
from haystack import indexes

from .models import Papers


class PaperIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    abstract = indexes.CharField(model_attr='abstract')
    year = indexes.CharField(model_attr='year')

    def get_model(self):
        return Papers

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(crawldate__lte=timezone.now())
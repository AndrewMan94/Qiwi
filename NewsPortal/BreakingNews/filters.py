from django_filters import FilterSet
from .models import *


# создаём фильтр
class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = ('id_author', 'rating', 'text',
                  'created')
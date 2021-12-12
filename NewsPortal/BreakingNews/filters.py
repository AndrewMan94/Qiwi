from django_filters import FilterSet
from .models import *



class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = ['author', 'rating', 'text',
                  'category']
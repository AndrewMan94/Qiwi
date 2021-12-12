from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import *


class PostForm(ModelForm):
    check_box = BooleanField(label='*')

    class Meta:
        model = Post
        fields = ['author', 'rating', 'category', 'text',
                  'check_box']
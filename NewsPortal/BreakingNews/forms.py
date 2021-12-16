from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, BooleanField
from .models import Post, Category


class PostForm(ModelForm):
    check_box = BooleanField(label='*')

class Meta:
    model = Post
    fields = ['id_author', 'rating', 'id_post_category', 'text']

class CategorySubscribersListForm(forms.ModelForm):

    subscribers = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
        required=False)


class CreatePostForm(ModelForm):
    category = forms.ModelMultipleChoiceField(label="Категория", queryset=Category.objects.all(),
                                              widget=forms.SelectMultiple(attrs={"style": "width:100%"}))
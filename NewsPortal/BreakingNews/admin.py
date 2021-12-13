from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']



class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'rating', 'author', 'dateCreation']


class AuthorAdmin(admin.ModelAdmin):
    fields = ['authorUser', 'ratingAuthor']


class CommentAdmin(admin.ModelAdmin):
    fields = ['commentPost', 'text', 'dateCreation', 'rating']

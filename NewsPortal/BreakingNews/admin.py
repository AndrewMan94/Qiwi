from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']



class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'rating', 'author', 'dateCreation']


class AuthorAdmin(admin.ModelAdmin):
    fields = ['authorUser', 'ratingAuthor']


class CommentAdmin(admin.ModelAdmin):
    fields = ['commentPost', 'text', 'dateCreation', 'rating']

class SubscribeAdmin(admin.ModelAdmin):
    fields = ['id_user', 'id_category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CategorySubscribers, SubscribeAdmin)
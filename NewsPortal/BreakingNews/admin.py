from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .models import *


class CategorySubscribersListForm(ChangeList):

    def __init__(self, request, model, list_display,
        list_display_links, list_filter, date_hierarchy,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin):

        super(CategorySubscribersListForm, self).__init__(request, model,
            list_display, list_display_links, list_filter,
            date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable,
            model_admin, search_help_text=None, sortable_by=None)

        self.list_display = ['name', 'subscribers']
        self.list_display_links = ['name']
        self.list_editable = ['subscribers']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']

class PostCategorySubscribersInline(admin.TabularInline):
    model = Category.subscribers.through

    def get_changelist(self, request, **kwargs):
        return CategorySubscribersListForm

    def get_changelist_form(self, request, **kwargs):
        return CategorySubscribersListForm



class AuthorAdmin(admin.ModelAdmin):
    fields = ['id_user', 'rating']

class PostAdmin(admin.ModelAdmin):
    fields = ['id_author', 'type', 'created', 'title', 'text', 'rating']
    list_filter = ['created', 'id_author']


class CommentAdmin(admin.ModelAdmin):
    fields = ['id_post', 'id_user', 'created', 'text', 'rating']

class CategorySubscribersAdmin(admin.ModelAdmin):
    fields = ['id_user', 'id_category']

class PostCategoryAdmin(admin.ModelAdmin):
    fields = ['id_post', 'id_category']


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CategorySubscribers, CategorySubscribersAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)


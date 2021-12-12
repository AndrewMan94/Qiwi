from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import CreateView
from . import apps
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def become_author(request):
    user = request.user
    authors = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors.user_set.add(user)
        author = apps.get_model('posts', 'Author')()
        author.id_user = user
        author.save()

    return redirect('/')

class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')

class AddPost(PermissionRequiredMixin, CreateView):
    permission_required = ('News.add_post', )

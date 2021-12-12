from django.views import View
from django.views.generic import ListView, DetailView
from .filters import PostFilter
from .models import *
from django.shortcuts import render
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    ordering = ['-rating']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
        queryset = self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)

    def form_class(self, POST):
        pass


class PostDetail(DetailView):
    model = Post
    context_object_name = 'Post'
    template_name = 'post.html'


class Posts(View):
    def get(self, request):
        posts = Post.objects.order_by('-rating')
        p = Paginator(posts, 1)
        posts = p.get_page(request.GET.get('page', 1))
        data = {
            'posts': posts,
        }
        return render(request, 'posts_list.html', data)


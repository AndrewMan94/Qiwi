from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .filters import PostFilter
from .models import *
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import PostForm, CreatePostForm


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    ordering = ['-rating']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)

    def form_class(self, POST):
        pass

class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()

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

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',
                           'news.change_post')
    template_name = 'post_create.html'
    form_class = CreatePostForm


class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


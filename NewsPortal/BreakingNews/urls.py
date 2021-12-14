from django.urls import path
from .views import *

urlpatterns = [
    path('post_list', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('post_create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
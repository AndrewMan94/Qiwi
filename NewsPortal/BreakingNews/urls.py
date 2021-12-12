from django.urls import path
from .views import *

urlpatterns = [
    path('postList', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
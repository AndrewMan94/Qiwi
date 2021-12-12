from django.urls import path
from .views import *

urlpatterns = [
    path('postList', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
]
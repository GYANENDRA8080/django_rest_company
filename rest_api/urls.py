from django.urls import path
from .views import PostsView, post_detail

urlpatterns = [
    path('posts/', PostsView),
    path('details/<int:pk>', post_detail),


]

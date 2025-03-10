from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    UserView,
)
from . import views

urlpatterns = [
    path('', views.about, name='blog-about'),
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/profile', UserView.as_view(), name='user-profile'), 
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('students/', views.people, name='students'),
    path('search/', views.search, name='search'),
]

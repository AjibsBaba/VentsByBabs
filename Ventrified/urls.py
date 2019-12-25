from . import views
from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]

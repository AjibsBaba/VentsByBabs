from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5




class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'gender']
    template_name = 'create.html'

    def form_valid(self, form):
        return super().form_valid(form)



class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

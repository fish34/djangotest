from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts_data = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts_data})

def post_detail(request, pk):
    posts_data = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': posts_data})
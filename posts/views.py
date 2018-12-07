from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
# Create your views here.

def homepageview(request):
    post = Post.objects.all()
    return render(request, 'posts/home.html', context={'posts':post})

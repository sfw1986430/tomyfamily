from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def homePageView(request):
     posts = Post.objects.all()
     return render(request,'blog/home.html', context={'posts':posts})

def blogDetailView(request,post_id):
     post_ = Post.objects.get(id=post_id)
     return render(request, 'blog/post_detail.html', context={'post_': post_})

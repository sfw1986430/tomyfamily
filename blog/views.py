from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Post
from .form import PostForm
from django.urls import reverse_lazy

# Create your views here.
def homePageView(request):
     posts = Post.objects.all()
     return render(request,'blog/home.html', context={'posts':posts})

def blogDetailView(request,post_id):
     post_ = Post.objects.get(id=post_id)
     return render(request, 'blog/post_detail.html', context={'post_': post_})

def blogCreatNewView(request):
     if request.method == "POST":
          form = PostForm(request.POST)
          if form.is_valid():
               post = form.save(commit=False)
               post.save()
               return redirect('post_detail', post_id=post.id)
     else:
          form = PostForm()

     return render(request, 'blog/post_new.html', context={'form':form})

def blogPostUpdateView(request,post_id):
     post_ = Post.objects.get(id=post_id)
     if request.method == "POST" :
          form = PostForm(data=request.POST,instance=post_)
          if form.is_valid():
               post_ = form.save(commit=False)
               # post_.title = request.title
               # post_.body = request.body
               post_.save()
               return redirect('post_detail', post_id=post_.id)
     else:
          form = PostForm()

     return render(request, 'blog/post_edit.html', context={'form': form})

def blogPostDeleteView(request, post_id):
     post_ = Post.objects.get(id=post_id)
     if request.method == "POST":
               post_.delete()
               return redirect(reverse_lazy('home'))
     else:
          form = PostForm(instance=post_)

     return render(request, 'blog/post_delete.html', context={'form': form, 'post_':post_})


               
          
          

     

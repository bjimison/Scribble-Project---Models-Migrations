from django.shortcuts import render
from .models import Post, Comment
# Create your views here.

def posts(request):
  posts = Post.objects.all()
  return render(request, 'scribble/post_list.html', {'posts':posts})

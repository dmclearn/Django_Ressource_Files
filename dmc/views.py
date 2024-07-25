from django.shortcuts import render

from Blog.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={"posts":posts})
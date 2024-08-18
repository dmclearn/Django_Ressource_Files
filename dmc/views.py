from django.shortcuts import render

from Blog.models import Post


def index(request):
    posts = Post.objects.all().order_by('-id')[:3]
    return render(request, 'index.html', context={"posts":posts})
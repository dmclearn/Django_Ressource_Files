from django.shortcuts import render

from Blog.models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, "blog/index.html", context={"posts":posts})

def post_show(request, slug:str):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/show.html", context={"post":post})
    pass
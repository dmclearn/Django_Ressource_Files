from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from Blog.forms import LoginForm, SignupForm
from Blog.models import CustomUser, Post

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, "blog/index.html", context={"posts":posts, 'nb_articles':len(posts)})

def post_show(request, slug:str):
    post = Post.objects.get(slug=slug)
    return render(request, "blog/show.html", context={"post":post})
    pass

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request=request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
            return redirect('homepage')
    
    return render(request, "blog/auth/my_login.html", {"form":form})
    pass

def my_logout(request):
    if request.user:
        logout(request)
        return redirect('homepage')
    return redirect("my_login")
    pass

def my_signup(request):
    form = SignupForm()
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = CustomUser.objects.get(username=data["username"])
            except CustomUser.DoesNotExist:
                user = CustomUser.objects.create_user(username=data["username"], password=data["password"])
                if user:
                    return redirect('my_login')
    return render(request, "blog/auth/my_signup.html", {"form":form})
    pass
"""
URL configuration for dmc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import  settings
from django.conf.urls.static import static

from Blog.views import my_login, my_logout, my_signup
from dmc.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    path('blog/', include("Blog.urls")),
    path('auth/login', my_login, name="my_login"),
    path('auth/signup', my_signup, name="my_signup"),
    path('auth/logout', my_logout, name="my_logout")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import index, post_show

urlpatterns = [
    path('', index, name="blog"),
    path('<str:slug>/', post_show, name="show_post")
]
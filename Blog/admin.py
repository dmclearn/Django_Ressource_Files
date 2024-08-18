from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.contrib.auth.hashers import make_password
 
from Blog.models import Category, CustomUser, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'description',
        'published_date',
        'author'
    ]
    
    exclude=['author', "slug",]
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        user = request.user
        author = None
        try:
            author = obj.author
            if not obj.author:
                author = user
        except:
            author = user
        finally:
            obj.author = author
        return super().save_model(request, obj, form, change)
    
    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        
        if (isinstance(obj, Post)):
            user = request.user
            author = obj.author
            if (user != author and user.role not in (CustomUser.ADMIN, CustomUser.EDITOR)):
                return False
            return super().has_change_permission(request, obj)
        return super().has_change_permission(request, obj)
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        if isinstance(obj, Post):
            user = request.user
            author = obj.author
            if (user != author and user.role not in (CustomUser.ADMIN, CustomUser.EDITOR)):
                return False
            return super().has_change_permission(request, obj)
            
        return super().has_delete_permission(request, obj)
        
    
    # def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    #     user = request.user
    #     queryset = super().get_queryset(request)
    #     if user.role not in (CustomUser.ADMIN, CustomUser.EDITOR):
    #         return queryset.filter(author=user)
    #     return queryset
    pass

class CustomUserAdmin(admin.ModelAdmin):
    exclude=('post_count',)
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if change:
            old_password = CustomUser.objects.get(pk=obj.id).password
            password = obj.password
            if old_password != password:
                obj.password = make_password(password)
        return super().save_model(request, obj, form, change)
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(CustomUser, CustomUserAdmin)
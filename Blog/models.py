from datetime import datetime 
from typing import Any
from django.db import models
from django.contrib.auth.models import User,AbstractUser, Permission, Group
from dmc.settings import AUTH_USER_MODEL


from django.utils.text import slugify

# Create your models here.

class CustomUser(AbstractUser):

    post_count = models.CharField(max_length=155)

    ADMIN = 0
    EDITOR = 1
    AUTHOR = 2
    VISITOR = 3

    choice = (
        (ADMIN, "Admin"),
        (EDITOR, "Editor"),
        (AUTHOR, "Author"),
        (VISITOR, "Visitor"),
    )

    role = models.PositiveSmallIntegerField(choices=choice, blank=True, null=True)

    age = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs) -> None:

        #Creation / Récuperation des groups
        admin_group, create_ad = Group.objects.get_or_create(name="Admin")
        editor_group, create_ed = Group.objects.get_or_create(name="Editor")
        author_group, create_auth = Group.objects.get_or_create(name="Author")
        visitor_group, create_vis = Group.objects.get_or_create(name="Visitor")

        #Recuperation des permission
        admin_permission = [
            Permission.objects.get(codename="add_post"),
            Permission.objects.get(codename="change_post"),
            Permission.objects.get(codename="delete_post"),
            Permission.objects.get(codename="view_post"),
            Permission.objects.get(codename="add_category"),
            Permission.objects.get(codename="change_category"),
            Permission.objects.get(codename="delete_category"),
            Permission.objects.get(codename="view_category"),
            Permission.objects.get(codename="add_customuser"),
            Permission.objects.get(codename="change_customuser"),
            Permission.objects.get(codename="delete_customuser"),
            Permission.objects.get(codename="view_customuser"),
        ]
        editor_permission = [
            Permission.objects.get(codename="add_post"),
            Permission.objects.get(codename="change_post"),
            Permission.objects.get(codename="delete_post"),
            Permission.objects.get(codename="view_post"),
            Permission.objects.get(codename="add_category"),
            Permission.objects.get(codename="change_category"),
            Permission.objects.get(codename="delete_category"),
            Permission.objects.get(codename="view_category"),
        ]

        author_permission = [
            Permission.objects.get(codename="add_post"),
            Permission.objects.get(codename="change_post"),
            Permission.objects.get(codename="view_post"),
            Permission.objects.get(codename="view_category"),
        ]

        visitor_permission = [
            Permission.objects.get(codename="view_post"),
            Permission.objects.get(codename="view_category"),
        ]

        admin_group.permissions.add(*admin_permission)
        editor_group.permissions.add(*editor_permission)
        author_group.permissions.add(*author_permission)
        visitor_group.permissions.add(*visitor_permission)
        match self.role:
            case self.ADMIN:
                self.is_active = True
                self.is_staff = True
                self.is_superuser =True

                self.groups.add(admin_group)

                return super().save(*args, **kwargs)
            case self.EDITOR:
                self.is_active = True
                self.is_staff = True
                self.is_superuser =False

                self.groups.add(editor_group)

                return super().save(*args, **kwargs)
            case self.AUTHOR:
                self.is_active = True
                self.is_staff = True
                self.is_superuser =False

                self.groups.add(author_group)

                return super().save(*args, **kwargs)
            case self.VISITOR:
                self.is_active = True
                self.is_staff = False
                self.is_superuser = False

                self.groups.add(visitor_group)

                return super().save(*args, **kwargs)
            case _:
                return super().save(*args, **kwargs)
    pass

class Category(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    pass

class Post(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    description = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=120, blank=True, null=True)
    published_date = models.DateField(default=datetime.now)
    category = models.ManyToManyField(to=Category, blank=True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    pass


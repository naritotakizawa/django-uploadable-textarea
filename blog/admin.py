from django.contrib import admin
from .forms import PostForm
from .models import Post


class PostAdmin(admin.ModelAdmin):
    form = PostForm


admin.site.register(Post, PostAdmin)

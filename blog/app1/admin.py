from django.contrib import admin
from .models import *


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_time', 'author')


admin.site.register(Blogs, BlogsAdmin)
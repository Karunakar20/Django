from django.contrib import admin
from . models import Blog,Blog_1

# Register your models here.
@admin.register(Blog)
class BlogRegister(admin.ModelAdmin):
    list_display = ('id', 'title','tags')


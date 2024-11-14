from django import forms
from .models import Blog

class BlogEditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'tags']

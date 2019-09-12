from django import forms
from .models import BlogPost

# Create your views here.
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content',]

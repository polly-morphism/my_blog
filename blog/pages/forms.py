from django import forms
from .models import BlogPost

# Create your views here.
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content',]


class BlogPostUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost

        fields = [
            "title", "content",
        ]

    def init(self, *args, **kwargs):
        super(UserUpdateForm, self).init(*args, **kwargs)

    def save(self, commit=True, user=None):
        instance: BlogPost = super(BlogPostUpdateForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance


class BlogPostDeleteForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = []

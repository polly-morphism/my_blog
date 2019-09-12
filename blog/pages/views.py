from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import BlogPost
from .forms import BlogPostForm

class BlogPostList(ListView):
    model = BlogPost
    template_name = "blogpost_list.html"

    def get_queryset(self):
        qs = BlogPost.objects.all()
        return qs

class BlogPostCreate(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blogpost_create.html"

    def get_success_url(self):
        return reverse('blogpost_create')


class BlogPostRetrieve(DetailView):
    model = BlogPost
    template_name = "blogpost_retrieve.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

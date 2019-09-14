from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm, BlogPostDeleteForm, BlogPostUpdateForm

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

class BlogPostUpdate(UpdateView):
    """
    Изменение информации о пользователе
    """
    model = BlogPost
    template_name = "blogpost_update.html"
    form_class = BlogPostUpdateForm

    def get_object(self):
        return get_object_or_404(BlogPost, slug=self.kwargs['slug'])

    def get_success_url(self):
        self.object.save()
        return '/blog/{}/'.format(self.kwargs['slug'])


class BlogPostDelete(DeleteView):
    """
    Удаление пользователя из системы
    """
    model = BlogPost
    template_name = "blogpost_delete.html"
    form_class = BlogPostDeleteForm

    def get_object(self, **kwargs):
        return get_object_or_404(BlogPost, slug=self.kwargs['slug'])

    def get_success_url(self):
        BlogPost.objects.filter(slug=self.kwargs['slug']).delete()
        return '/blog/list/'

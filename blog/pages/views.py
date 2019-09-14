from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm, BlogPostDeleteForm, BlogPostUpdateForm

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogPostSerializer


class BlogPostListREST(APIView):
    """
    REST List all posts, or create a new post.
    """
    def get(self, request, format=None):
        blogposts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostDetailREST(APIView):
    """
    REST Retrieve, update or delete a blog post instance.
    """
    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blogpost = self.get_object(pk)
        serializer = BlogPostSerializer(blogpost)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        blogpost = self.get_object(pk)
        serializer = BlogPostSerializer(blogpost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blogpost = self.get_object(pk)
        blogpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class BlogPostList(ListView):
    """
    List all blog posts with generic views
    """
    model = BlogPost
    template_name = "blogpost_list.html"

    def get_queryset(self):
        qs = BlogPost.objects.all()
        return qs

class BlogPostCreate(CreateView):
    """
    Create a blog post with generic views
    """
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blogpost_create.html"

    def get_success_url(self):
        return reverse('blogpost_create')


class BlogPostRetrieve(DetailView):
    """
    Get/Retrieve post
    """
    model = BlogPost
    template_name = "blogpost_retrieve.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogPostUpdate(UpdateView):
    """
    Update and change post
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
    Delete post
    """
    model = BlogPost
    template_name = "blogpost_delete.html"
    form_class = BlogPostDeleteForm

    def get_object(self, **kwargs):
        return get_object_or_404(BlogPost, slug=self.kwargs['slug'])

    def get_success_url(self):
        BlogPost.objects.filter(slug=self.kwargs['slug']).delete()
        return '/blog/list/'

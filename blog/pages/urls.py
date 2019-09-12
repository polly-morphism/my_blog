from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.BlogPostList.as_view(), name='blogpost_list'),
    path('create/', views.BlogPostCreate.as_view(), name='blogpost_create'),
    path('<slug:slug>/', views.BlogPostRetrieve.as_view(), name='blogpost_retrieve'),
]

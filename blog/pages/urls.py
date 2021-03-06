from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('list/', views.BlogPostList.as_view(), name='blogpost_list'),
    path('create/', views.BlogPostCreate.as_view(), name='blogpost_create'),
    path('<slug:slug>/', views.BlogPostRetrieve.as_view(), name='blogpost_retrieve'),
    path('<slug:slug>/update/', views.BlogPostUpdate.as_view(), name='blogpost_update'),
    path('<slug:slug>/delete/', views.BlogPostDelete.as_view(), name='blogpost_detele'),

    # 
    # path('blogposts/', views.BlogPostListREST.as_view()),
    # path('blogposts/<slug:slug>/', views.BlogPostDetailREST.as_view()),
]

from django.contrib import admin
from django.urls import path, re_path, include
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('pages.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    path('blogposts/', views.BlogPostListREST.as_view()),
    path('blogposts/<int:pk>/', views.BlogPostDetailREST.as_view()),

    path('', include('frontend.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

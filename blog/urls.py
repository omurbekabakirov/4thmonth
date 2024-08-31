"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post.views import (
    main_view,
    post_list_view,
    post_detail_view,
    post_create_view,
    post_update_view,
    PostListView,
    PostDetailView,
    PostCreateView,
)
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('post_lst/', post_list_view, name='post_lst'),
    path('posts/<int:post_id>/', post_detail_view, name='post_detail'),
    path('posts/create/', post_create_view, name='post_create'),
    path('user/register/', views.register_view, name='register_view'),
    path('user/login/', views.login_view),
    path('user/logout/', views.logout_view, name='logout_view'),
    path('user/profile/', views.profile_view, name='profile_view'),
    path('posts/<int:post_id>/update', post_update_view, name='post_update'),
    path('posts2/', PostListView.as_view(), name='plv'),
    path('postsdetai2/', PostDetailView.as_view(), name='pdv'),
    path('posts22/', PostCreateView.as_view(), name='pcv'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

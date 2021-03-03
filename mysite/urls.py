"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
# from django.contrib.auth import views
from django.conf.urls import url, include
from blog.resources import PostResource, CommentResource

post_resource = PostResource()
comment_resource = CommentResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r'^postapi/', include(post_resource.urls)),
    url(r'^commentapi/', include(comment_resource.urls)),
    # url(r'^api/comments', include(comment_resource.urls)),
    # path('accounts/login/', views.LoginView.as_view(), name='login'), # the views here refers to the import
    # path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls'))  # default shows the blog urls
]

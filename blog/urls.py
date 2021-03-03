from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"), # default is the list of posts
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name="post_edit"),
    path('post/<int:pk>/delete/', views.post_delete, name="post_delete"),
    path('drafts/', views.drafts, name="drafts"),
    path('post/<pk>/publish/', views.publish, name="post_publish"),
    path('post/<int:pk>/add_comment', views.add_comment, name="add_comment"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<str:id>/detail/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<str:id>/edit/', views.post_edit, name='post_edit'),
    path('post/<str:id>/delete/', views.post_delete, name='post_delete'),
    path('post/draft', views.post_draft_list, name='post_draft'),
    path('post/<str:id>/publish', views.post_publish, name='post_publish'),
    path('post/<str:id>/comment', views.post_comment, name='post_comment'),
    path('comment/<str:comment_id>/delete', views.comment_delete, name='comment_delete'),
    path('comment/<str:comment_id>/approve', views.comment_approve, name='comment_approve'),
]
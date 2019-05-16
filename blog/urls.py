from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('add/', views.PostAdd.as_view(), name='post_add'),
    path('upload/', views.upload, name='upload'),
]

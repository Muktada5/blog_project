from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', views.add_post, name='add_post'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.owners, name='owners'),

    # Categories
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('new-category/', views.create_category, name='create_category'),

    # Posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<int:pk>/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),

    
]

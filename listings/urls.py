from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('new/', views.new_listing, name='new_listing'),
    path('listing/<int:pk>/edit/', views.edit_listing, name='edit_listing'),
    path('listing/<int:pk>/delete/', views.delete_listing, name='delete_listing'),
]

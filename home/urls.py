from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('amenities/', views.amenities, name='amenities'),
    path('dockwa/', views.dockwa, name='dockwa'),
    path('marriott/',views.marriott, name='marriott'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('calendar/', views.cal, name='cal'),
    path('contact/',  views.contact, name='contact'),
    path('listings/', views.listings, name='listings'),
    path('owners/',  views.owners, name='owners'),


]

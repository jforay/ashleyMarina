from django.urls import path
from . import views

urlpatterns = [
    path('', views.owners, name='owners'),
    
]

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def home(request):
    categories = [
        {"name":"Marina Amenities", "image_url":"/static/home/images/categories/amenities.jpg", "link":"#"},
        {"name":"Dockwa", "image_url":"/static/home/images/categories/dockwa.png", "link":"#"},
        {"name":"Marriott Rates", "image_url":"/static/home/images/categories/marriott.jpg", "link":"#"},
        {"name":"FAQ", "image_url":"/static/home/images/categories/FAQ.jpeg", "link":"#"},
        {"name":"Event Calendar", "image_url":"/static/home/images/categories/calendar.jpg", "link":"#"},
        {"name":"Contact", "image_url":"/static/home/images/categories/contact.jpg", "link":"#"},
        {"name":"Listings", "image_url":"/static/home/images/categories/listings.jpg", "link":"#"},
        {"name":"Owners", "image_url":"/static/home/images/categories/owners.jpg", "link":"#"},
    ]
    return render(request, 'home/home.html', {'categories':categories})

def amenities(request):
    return render(request, 'homoe/amenities.html')

def cal(request):
    return render(request, 'home/cal.html')

def dockwa(request):
    return render(request, 'home/dockwa.html')

def marriott(request):
    return render(request, 'home/marriott.html')

def FAQ(request):
    return render(request, 'home/faq.html')

def contact(request):
    return render(request, 'home/contact.html')

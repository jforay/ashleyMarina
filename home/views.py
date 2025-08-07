from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import ContactMessageForm

def home(request):
    categories_big = [
        {"name":"Marina Amenities", "image_url":"/static/home/images/categories/amenities-big.jpeg", "link":reverse('amenities')},
        {"name":"Dockwa", "image_url":"/static/home/images/categories/dockwa-big.jpeg", "link":reverse('dockwa')},
        {"name":"Event Calendar", "image_url":"/static/home/images/categories/calendar-big.jpg", "link":reverse('cal')},
        {"name":"Current Listings", "image_url":"/static/home/images/categories/listings-big.jpeg", "link":reverse('listings')},
        {"name":"Marriott Rates", "image_url":"/static/home/images/categories/marriott-big.jpg", "link":reverse('marriott')},  
        {"name":"FAQs", "image_url":"/static/home/images/categories/faqs-big.jpeg", "link":reverse('FAQ')},
        {"name":"Contact Us", "image_url":"/static/home/images/categories/contact-us-big.jpeg", "link":reverse('contact')},
        {"name":"Owners Forum", "image_url":"/static/home/images/categories/owners-big.jpeg", "link":reverse('owners')},
    ]
    categories_medium = [
        {"name":"Marina Amenities", "image_url":"/static/home/images/categories/amenities-big.jpeg", "link":reverse('amenities')},
        {"name":"Dockwa", "image_url":"/static/home/images/categories/dockwa-big.jpeg", "link":reverse('dockwa')},
        {"name":"Event Calendar", "image_url":"/static/home/images/categories/calendar-big.jpg", "link":reverse('cal')},
        {"name":"Current Listings", "image_url":"/static/home/images/categories/listings-big.jpeg", "link":reverse('listings')},
        {"name":"Marriott Rates", "image_url":"/static/home/images/categories/marriott-big.jpg", "link":reverse('marriott')},  
        {"name":"FAQs", "image_url":"/static/home/images/categories/faqs-big.jpeg", "link":reverse('FAQ')},
        {"name":"Contact Us", "image_url":"/static/home/images/categories/contact-us-big.jpeg", "link":reverse('contact')},
        {"name":"Owners Forum", "image_url":"/static/home/images/categories/owners-big.jpeg", "link":reverse('owners')},
    ]
    categories_small = [
        {"name":"Marina Amenities", "image_url":"/static/home/images/categories/amenities-big.jpeg", "link":reverse('amenities')},
        {"name":"Dockwa", "image_url":"/static/home/images/categories/dockwa-small.jpeg", "link":reverse('dockwa')},
        {"name":"Event Calendar", "image_url":"/static/home/images/categories/calendar-big.jpg", "link":reverse('cal')},
        {"name":"Current Listings", "image_url":"/static/home/images/categories/listings-small.jpeg", "link":reverse('listings')},
        {"name":"Marriott Rates", "image_url":"/static/home/images/categories/marriott-big.jpg", "link":reverse('marriott')},  
        {"name":"FAQs", "image_url":"/static/home/images/categories/faqs-small.jpeg", "link":reverse('FAQ')},
        {"name":"Contact Us", "image_url":"/static/home/images/categories/contact-us-small.jpeg", "link":reverse('contact')},
        {"name":"Owners Forum", "image_url":"/static/home/images/categories/owners-small.jpeg", "link":reverse('owners')},
    ]
    return render(request, 'home/home.html', {'categories_big':categories_big,'categories_medium':categories_medium,'categories_small':categories_small})

def amenities(request):
    return render(request, 'home/amenities.html')

def cal(request):
    return render(request, 'home/cal.html')

def dockwa(request):
    return render(request, 'home/dockwa.html')

def marriott(request):
    return render(request, 'home/marriott.html')

def FAQ(request):
    return render(request, 'home/faq.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/contact_success.html')  # simple thank you page
    else:
        form = ContactMessageForm()

    return render(request, 'home/contact.html', {'form': form})

def terms(request):
    return render(request, 'home/terms_of_use.html')

def privacy(request):
    return render(request,'home/privacy_policy.html')
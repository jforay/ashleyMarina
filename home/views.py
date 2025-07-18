from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import ContactMessageForm

def home(request):
    categories = [
        {"name":"Marina Amenities", "image_url":"/static/home/images/categories/amenities2.jpeg", "link":reverse('amenities')},
        {"name":"Dockwa", "image_url":"/static/home/images/categories/dockwa2.jpeg", "link":reverse('dockwa')},
        {"name":"Event Calendar", "image_url":"/static/home/images/categories/calendar.jpg", "link":reverse('cal')},
        {"name":"Current Listings", "image_url":"/static/home/images/categories/listings2.jpeg", "link":reverse('listings')},
        {"name":"Marriott Rates", "image_url":"/static/home/images/categories/marriott.jpg", "link":reverse('marriott')},  
        {"name":"FAQs", "image_url":"/static/home/images/categories/faqs.jpeg", "link":reverse('FAQ')},
        {"name":"Contact Us", "image_url":"/static/home/images/categories/contact-us2.jpeg", "link":reverse('contact')},
        {"name":"Owners Forum", "image_url":"/static/home/images/categories/owners4.jpeg", "link":reverse('owners')},
    ]
    return render(request, 'home/home.html', {'categories':categories})

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
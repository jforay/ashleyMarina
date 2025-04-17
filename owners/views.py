from django.shortcuts import render

# Create your views here.

def owners(request):
    return render(request, 'owners/owners.html')
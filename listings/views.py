from django.shortcuts import render



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Listing
from .forms import ListingForm

# Create your views here
def listings(request):
    listings = Listing.objects.filter(is_active=True)

    return  render(request, 'listings/listings.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

@user_passes_test(lambda u: u.is_superuser)
def new_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings')
    else:
        form = ListingForm()
    return render(request, 'listings/new_listing.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def edit_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    form = ListingForm(request.POST or None, request.FILES or None, instance=listing)
    if form.is_valid():
        form.save()
        return redirect('listing_detail', pk=pk)
    return render(request, 'listings/edit_listing.html', {'form': form, 'listing': listing})

@user_passes_test(lambda u: u.is_superuser)
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        listing.delete()
        return redirect('listings')
    return render(request, 'listings/confirm_delete.html', {'object': listing, 'type': 'Listing'})

# collection/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Gown, MaidsDress, WeddingVideo

# ---------------- HOME ----------------
def home(request):
    collection_gowns = Gown.objects.filter(category='collection')
    party_dresses = Gown.objects.filter(category='party')
    videos = WeddingVideo.objects.all()
    return render(request, 'collection/home.html', {
        'collection_gowns': collection_gowns,
        'party_dresses': party_dresses,
        'videos': videos,
    })

# ---------------- GOWNS ----------------
def gowns(request):
    collection_gowns = Gown.objects.filter(category='collection')
    return render(request, 'collection/gowns.html', {
        'collection_gowns': collection_gowns,
    })

# ---------------- PARTY DRESSES ----------------
def party_dresses(request):
    party_dresses = Gown.objects.filter(category='party')
    return render(request, 'collection/party.html', {
        'party_dresses': party_dresses,
    })

# ---------------- MAIDS DRESSES ----------------
def maids_dresses(request):
    dresses = MaidsDress.objects.all()
    return render(request, 'collection/maids_dresses.html', {'maids_dresses': dresses})

# ---------------- WEDDING VIDEOS ----------------
def wedding_videos(request):
    videos = WeddingVideo.objects.all()
    return render(request, 'collection/videos.html', {'videos': videos})

# ---------------- ABOUT US ----------------
def about_us(request):
    return render(request, 'collection/about_us.html')

# ---------------- SEARCH ----------------
def search(request):
    query = request.GET.get('q', '').strip()
    gowns = Gown.objects.filter(name__icontains=query) if query else []
    videos = WeddingVideo.objects.filter(title__icontains=query) if query else []
    return render(request, 'collection/search_results.html', {
        'query': query,
        'gowns': gowns,
        'videos': videos,
    })

# ---------------- SHARED DETAIL VIEW ----------------
def gown_detail(request, gown_id, source=None):
    """
    Shared detail view for Gown, Party Dress, and Maids Dress.
    `source` determines which "Back to" link to show in the template.
    """
    # Try to get Gown (collection or party)
    gown = Gown.objects.filter(id=gown_id).first()
    
    # If not found in Gown, try MaidsDress
    if not gown:
        gown = MaidsDress.objects.filter(id=gown_id).first()
    
    # If still not found, return 404
    if not gown:
        return HttpResponse("Item not found", status=404)
    
    return render(request, 'collection/gown_detail.html', {
        'gown': gown,
        'source': source,  # will be 'party', 'maids', or None for collection gowns
    })


# ---------------- NEW CATEGORIES ----------------
def casual(request):
    # Placeholder page for casual clothing
    return render(request, 'collection/casual.html')

def shoes(request):
    return render(request, 'collection/shoes.html')

def bags(request):
    return render(request, 'collection/bags.html')

def lingeries(request):
    return render(request, 'collection/lingeries.html')

def jewelry(request):
    return render(request, 'collection/jewelry.html')

def traditional_clothes(request):
    return render(request, 'collection/traditional_clothes.html')

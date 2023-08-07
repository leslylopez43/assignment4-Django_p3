from django.shortcuts import render 
from .models import Item
# Create your views here.

def  get_venue_list(request):
    items = Item.objects.all()
    context = {
        "items" : items
    }
    return render(request, "venue/venue_list.html", context)
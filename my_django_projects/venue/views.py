from django.shortcuts import  render, redirect
from .models import Item

# Create your views here.

def  get_venue_list(request):
    items = Item.objects.all()
    context = {
        "items" : items
    }
    return render(request, "venue/venue_list.html", context)

def  get_tenant(request):
    items = Item.objects.all()
    context = {
        "items" : items
    }
    return render(request, "venue/tenant.html", context)

def  add_tenant_item(request):
    if request.method == "POST" :
        name = request.POST.get("item_name")
        done = "done" in request.POST
        Item.objects.create(name=name, done=done)
        
        return  redirect ("get_tenant")
    return render(request, '/add_tenant.html',)
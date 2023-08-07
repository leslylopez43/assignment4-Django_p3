from django.shortcuts import render 

# Create your views here.
def  get_venue_list(request):
        return render(request, "venue/venue_list.html")
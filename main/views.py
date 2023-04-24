from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from .models import Artwork
# Create your views here.
def homepage(request):
    return render(request = request, 
                  template_name = "main/home.html", 
                  context= {"videos": Video.objects.all,
                            }
                  )

def artwork(request):
    return render(request,
                  "main/artwork.html",
                  {"artwork": Artwork.objects.all})
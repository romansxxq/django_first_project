from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def artist_details(request):
    return render(request, 'artist_details.html')
def details(request):
    return HttpResponse("<h1>Details</h1>")
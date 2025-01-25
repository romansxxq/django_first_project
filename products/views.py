from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def biography(request):
    return render(request, 'biography.html')

def picture(request):
    return render(request, 'pictures.html')

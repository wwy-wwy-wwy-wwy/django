from django.http import HttpResponse
from django.shortcuts import render
# from .models import *


# Create your views here.



def weather_view(request):
    m = request.method
    if m == 'POST':
        return render(request, 'temp.html')
    else:
        return render(request, 'weather.html')
    return render(request,'weather.html')

def temp_view(request):
    return render(request,'temp.html')


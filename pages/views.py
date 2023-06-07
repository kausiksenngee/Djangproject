from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here
# Setting up Home page View
def homePageView(request):
    
    return HttpResponse("Hello Django Nice to Meet you")
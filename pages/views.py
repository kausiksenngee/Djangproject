from django.shortcuts import render

from django.views.generic import TemplateView

from django.views.generic import ListView,DetailView
from .models import Post
#Create class based view for homepageview inherit ListView
class HomePageView(ListView):
    model=Post
    template_name='home.html'

# Create class based view for DetailsView inherit from DetailView    
class DetailView(DetailView):
    model=Post
    template_name="post_details.html"


class Aboutpageview(TemplateView):
    template_name='about.html'

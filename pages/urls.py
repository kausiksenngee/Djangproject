# import path to power our url patterns
from django.urls import path
# import view.py files to look up homePageView Method
from .views import HomePageView,Aboutpageview,DetailView

urlpatterns =[
    path("",HomePageView.as_view(),name="home"),
    path("about/",Aboutpageview.as_view(),name="about"),
    path("post/<int:pk>/",DetailView.as_view(),name="post_details"),
]

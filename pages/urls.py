# import path to power our url patterns
from django.urls import path
# import view.py files to look up homePageView Method
from .views import homePageView

urlpatterns =[
    path("",homePageView,name="home")
]

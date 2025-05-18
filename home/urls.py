from django.urls import path
from . import views


'''
This allows for the home model and template to load on the main url
'''


urlpatterns = [
    path('', views.home_page, name="index")
]

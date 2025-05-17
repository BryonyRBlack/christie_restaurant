from . import views
from django.urls import path

'''
This is in place to show how the wanted list should be displayed
The path also confirms the url structure.
'''

urlpatterns = [
    path("wanted", views.WantedList.as_view(), name="wanted"),
]
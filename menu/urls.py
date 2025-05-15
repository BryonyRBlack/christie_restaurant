from . import views
from django.urls import path

urlpatterns = [
    path('menu', views.WantedList.as_view(), name='menu'),
]
from . import views
from django.urls import path

urlpatterns = [
    path('wanted', views.WantedList.as_view(), name='wanted'),
]
from . import views
from django.urls import path

urlpatterns = [
    path('menu', views.FoodList.as_view(), name='menu'),
]
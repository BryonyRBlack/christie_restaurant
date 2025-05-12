from . import views
from django.urls import path

urlpatters = [
    path('menu', views.PostList.as_view(), name='menu')
]
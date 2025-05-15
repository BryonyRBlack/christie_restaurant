"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from reviews.views import my_reviews
from contact.views import contact_us
from menu.views import wanted_list
from booking import views
#from news.views import article_list
#from home.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('booking/', views.CreateView.as_view(), name='booking'),
    path('reviews/', my_reviews, name='review'),
    path('contact/', contact_us, name='contact_us'),
    path('', include("home.urls"), name='home-urls'),
    path('menu/', wanted_list, name='menu'),
    path('news/', include("news.urls"), name='news')
]

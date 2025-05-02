from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
from . forms import ReviewForms

# Create your views here.
def my_reviews(request):
    review_form = ReviewForms

    return render(
        request,
        "reviews/reviews.html",
        {
            "review_form":review_form, 
        }   
    )
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from .models import Review
from . forms import ReviewForms

# Create your views here.

class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1)
    template_name = "reviews/reviews.html"


def my_reviews(request):
    review = Review.objects.all().order_by('-created_at')
    review_form = ReviewForms


    return render(
        request,
        "reviews/reviews.html",
        {
            "review_form": review_form,
            "review": review,
        }   
    )
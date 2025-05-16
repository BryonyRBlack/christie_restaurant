from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Review
from . forms import ReviewForms

# Create your views here.

#class ReviewList(generic.ListView):
    #queryset = Review.objects.filter(status=1)
    #template_name = "reviews/reviews.html"


#def my_reviews(request):
    #review = Review.objects.all().order_by('-created_at')
    #review_form = ReviewForms


    #return render(
        #request,
        #"reviews/reviews.html",
        #{
            #"review_form": review_form,
            #"review": review,
        #}   
    #)

def my_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    

    if request.method == "POST":
        review_form = ReviewForms(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.post = reviews
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted succesfully'
            )

    review_form = ReviewForms

    return render(
        request,
        'reviews/reviews.html',
        {
            'reviews': reviews,
            'review_form': review_form
        }
    )
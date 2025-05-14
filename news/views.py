from django.shortcuts import render
from .models import Post
from django.http import Http404

# Create your views here.
def article_list(request):
    articles = Post.published.all()

    return render(
        request,
        'news/news.html',
        {'articles': articles}
    )
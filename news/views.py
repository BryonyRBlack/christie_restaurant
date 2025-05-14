from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Post

# Create your views here.
class ArticleList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'news/news.html'

    #def article_list(request):
        #articles = Post.objects.filter(status=1)

        #return render(
            #request,
            #'news/news.html',
            #{'articles': articles}
    #)

def article_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "news/article_detail.html",
        {"article": article}
    )
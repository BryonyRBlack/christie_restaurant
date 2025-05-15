from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages

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
    comments = article.comments.all().order_by("-posted")
    comment_form = CommentForm

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = comments
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted succesfully'
            )

    return render(
        request,
        "news/article_detail.html",
        {"article": article,
        "comments": comments,
        "comment_form": comment_form
        }
    )
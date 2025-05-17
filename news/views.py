from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Article, Comment
from .forms import CommentForm

'''
This allows for all published articles to be visible on the front end.
It also shows the comment form, and if the user is logged in, they are able to leave a comment, and receive confirmation.
'''
# Create your views here.
class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1)
    template_name = "news/news.html"


def article_detail(request, slug):
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    comments = article.comments.all().order_by("-posted")
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Comment submitted succesfully"
            )

    comment_form = CommentForm

    return render(
        request,
        "news/article_detail.html",
        {"article": article,
         "comments": comments,
         "comment_form": comment_form
        }
    )

'''
If a user is logged in and has previously left a comment, this allows them to edit the comment.
If this is done succesfully, they receive a confirmation message
'''

def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.post = article
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment updated succesfully")
        else:
            messages.add_message(request, messages.ERROR, "This has not been successful")

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))

'''
If a user is logged in and previously left a comment, this allows them to delete the comment.
If this is successful, they receive a confirmation message.
'''

def comment_delete(request, slug, comment_id):
    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted")
    else:
        messages.add_message(request, messages.ERROR, "This has not been deleted")

    return HttpResponseRedirect(reverse("article_detail", args=[slug]))
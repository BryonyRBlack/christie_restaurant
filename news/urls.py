from django.urls import path
from . import views

'''
The url patters allow for the ability to click on an article name
and generate the whole article.
They also allow for comments to be edited and deleted.
'''

urlpatterns = [
    path('', views.ArticleList.as_view(), name="news"),
    path('<slug:slug>/', views.article_detail, name="article_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit,
         name="comment_edit"),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete,
         name="comment_delete"),
]

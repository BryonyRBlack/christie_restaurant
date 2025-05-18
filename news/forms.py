from django import forms
from .models import Comment


'''
The comment form allows the user to leave a comment on the article.
It requires the user to be logged in, a place for a message, and a rating.
'''


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body", "rating",)

from django import forms
from comment_app.models import Comment

class AddingCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
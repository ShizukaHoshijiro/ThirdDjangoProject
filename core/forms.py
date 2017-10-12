from django import forms
from .models import Comment

class IndexPageForm(forms.Form):
    search_field = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(("-pub_date", "Дата создания"), ("-article_rating", "Рейтинг"), ("comments_count", "Количество комментариев")),required=False)
    # Формы сортировки

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

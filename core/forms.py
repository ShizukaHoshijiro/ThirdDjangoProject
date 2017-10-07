from django import forms

class IndexPageForm(forms.Form):
    search_field = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(("-topic_pub_date", "Дата создания"), ("-article_rating", "Рейтинг"), ("comments_count", "Количество комментариев")),required=False)
    # Формы сортировки
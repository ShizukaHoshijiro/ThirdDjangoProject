from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from core.models import Topic

class IndexView(ListView):
    model = Topic
    template_name = "core/index.html"

class Topic_DetailView(DetailView):
    model = Topic
    template_name = "core/detail.html"

    # pk_url_kwarg = "topic_id"
    # Определяет под каким именем будет извлечён индетификатор объекта, из regex или GET запроса.



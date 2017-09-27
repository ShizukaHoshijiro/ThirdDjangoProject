from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from core.models import Topic

class IndexView(ListView):
    model = Topic
    template_name = "core/index.html"




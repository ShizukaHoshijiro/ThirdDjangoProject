from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from core.models import Topic
from django.contrib import messages
from django.urls import reverse


class IndexView(ListView):
    model = Topic
    template_name = "core/index.html"

class Topic_DetailView(DetailView):
    model = Topic
    template_name = "core/detail.html"
    # pk_url_kwarg = "topic_id" ---deleted
    # Определяет под каким именем будет извлечён индетификатор объекта, из regex или GET запроса.

class Topic_CreateView(CreateView):
    model = Topic
    template_name = "core/create.html"
    fields = ("topic_title","topic_description")

    def form_valid(self, form):
        form.instance.topic_author = self.request.user
        return super(Topic_CreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(Topic_CreateView, self).post(request, *args,**kwargs)
        else:
            redirect_url = reverse("login")
            redirect_url = redirect_url + "?next=" + request.path
            return redirect(redirect_url)
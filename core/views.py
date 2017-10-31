from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from .models import Topic
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from core.forms import IndexPageForm
from django.contrib.contenttypes.models import ContentType,ContentTypeManager
from django.http import Http404
# from core.forms import CommentForm
from django.contrib.auth.decorators import login_required
from comment_app.forms import CommentForm
from django.db.models import Q
from django.db import models

class IndexView(ListView):
    model = Topic
    template_name = "core/index.html"


class TopicsListView(ListView):
    model = Topic
    template_name = "core/list.html"

    def dispatch(self, request, *args, **kwargs):
        self.form = IndexPageForm(request.GET)
        # Search_form
        self.form.is_valid()
        return super(TopicsListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):

        def search_by(queryset_input, search_field_input):
            if search_field_input:
                queryset_input = queryset_input.filter(Q(title__icontains=search_field_input) | Q(description__icontains=search_field_input))
            return queryset_input

        def sort_by(queryset_input, sort_field_input):
            if sort_field_input == "pub_date":
                queryset_input = queryset_input.order_by("-pub_date")
            elif sort_field_input == "comments_count":
                queryset_input = queryset_input.annotate(comments_count=models.Count("comments")).order_by("-comments_count")
            elif sort_field_input == "likes_count":
                queryset_input = queryset_input.annotate(likes_count=models.Count("likes")).order_by("-likes_count")
            return queryset_input

        # self.a = Topic.objects.annotate(comments_count=models.Count("comments"))
        # self.b = Topic.objects.annotate(likes_count=models.Count("likes"))
        # Примеры агрегирования данных

        self.queryset = Topic.objects.all()
        # Изначальный queryset, выборка по умолчанию.

        sort_field = self.form.cleaned_data.get("sort_field","-pub_date")
        search_field = self.form.cleaned_data.get("search_field",None)
        # метод get возвращает чначение с указанным ключём или второй аргумент если он равен None

        self.queryset = search_by(self.queryset,search_field)
        self.queryset = sort_by(self.queryset, sort_field)

        return self.queryset[0:40]





        """        def search_by(queryset,search_field):
            if search_field:
                queryset = queryset.filter(Q(title__icontains=search_field)|Q(description__icontains=search_field))
            return queryset

        sort_field = self.form.cleaned_data.get("sort_field","-pub_date")
        search_field = self.form.cleaned_data.get("search_field",None)
        # метод get возвращает чначение с указанным ключём или второй аргумент если он равен None

        self.a = Topic.objects.annotate(comments_count=models.Count("comments"))
        self.b = Topic.objects.annotate(like_count=models.Count("likes"))
        # Примеры агрегирования данных

        if sort_field == "":
            sort_field = "-pub_date"

        self.queryset = search_by(self.queryset,search_field)
        

        return self.queryset[0:40]
"""



    def get_context_data(self, **kwargs):
        context = super(TopicsListView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context


class TopicDetailView(DetailView):
    model = Topic
    template_name = "core/detail.html"
    # pk_url_kwarg = "topic_id" ---deleted
    # Определяет под каким именем будет извлечён индетификатор объекта, из regex или GET запроса.
    def get(self, request, *args, **kwargs):
        self.form = CommentForm
        return super(TopicDetailView, self).get(request,*args,**kwargs)
    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context


class TopicCreateView(CreateView):
    model = Topic
    template_name = "core/create.html"
    fields = ("title","description")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TopicCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(TopicCreateView, self).post(request, *args,**kwargs)
        else:
            redirect_url = reverse("login")
            redirect_url = redirect_url + "?next=" + request.path
            return redirect(redirect_url)


class UserRegisterView(FormView):
    form_class = UserCreationForm
    template_name = "core/register.html"

    def get_success_url(self):
        success_url = self.request.GET.get("next",reverse("core:index"))
        if success_url == reverse("login") or success_url == reverse("logout") or success_url == reverse("register"):
            success_url = reverse("core:index")
        return success_url

    def form_valid(self, form):
        super(UserRegisterView, self).form_valid(form)
        form.save()

        user = authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password1"])
        if user is not None:
            login(self.request,user)

        return HttpResponseRedirect(self.get_success_url())

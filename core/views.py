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

class IndexView(ListView):
    model = Topic
    template_name = "core/index.html"

    def dispatch(self, request, *args, **kwargs):
        self.form = IndexPageForm(request.GET)
        self.form.is_valid()
        return super(IndexView, self).dispatch(request,*args,**kwargs)

    def get_queryset(self):

        sort_field = self.form.cleaned_data.get("sort_field","-pub_date")
        search_field = self.form.cleaned_data.get("search_field",None)
        # метод get возвращает чначение с указанным ключём или второй аргумент если он равен None

        if sort_field == "":
            sort_field = "-pub_date"
        if search_field == "":
            search_field = None

        if search_field is not None:
            self.queryset = Topic.objects.order_by(sort_field).filter(title__icontains=search_field)
        else:
            self.queryset = Topic.objects.order_by(sort_field)
        return self.queryset[0:40]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context

class Topic_DetailView(DetailView):
    model = Topic
    template_name = "core/detail.html"
    # pk_url_kwarg = "topic_id" ---deleted
    # Определяет под каким именем будет извлечён индетификатор объекта, из regex или GET запроса.
    def get(self, request, *args, **kwargs):
        self.form = CommentForm
        return super(Topic_DetailView, self).get(request,*args,**kwargs)
    def get_context_data(self, **kwargs):
        context = super(Topic_DetailView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context

class Topic_CreateView(CreateView):
    model = Topic
    template_name = "core/create.html"
    fields = ("title","description")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(Topic_CreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(Topic_CreateView, self).post(request, *args,**kwargs)
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

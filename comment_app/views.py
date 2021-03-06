from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse, HttpResponseNotAllowed
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormView
from comment_app.models import Comment
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from core.forms import IndexPageForm
from django.contrib.contenttypes.models import ContentType,ContentTypeManager
from django.http import Http404
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json


@login_required
def add_comment(request):

    form = CommentForm(request.POST)
    form.is_valid()
    comment_content = form.cleaned_data.get("content",None)

    model_name = request.POST.get("model_name",None) # Имя модели в, обязательно, нижнем регистре.
    object_id = request.POST.get("object_id",None)
    app_label = request.POST.get("app_label", "core")

    if model_name and object_id and comment_content:

        # Получает экземпляр ContentType для текущей модели
        content_type_for_model = ContentType.objects.get(app_label=app_label,model=model_name)
        # app_label - название/имя приложения; model - имя модели.
        # Для большей информации - https://djbook.ru/rel1.9/ref/contrib/contenttypes.html

        this_object = content_type_for_model.get_object_for_this_type(id=object_id)
        # Получаем текущий объект,
        # get_object_for_this_type - аналог get(), получает объект из выборки всех объектов модели предстовляемой данным экземпляром ContentType
        # Пздц всё сложно.

        new_comment = Comment()
        new_comment.content = comment_content
        new_comment.author = request.user
        new_comment.object = this_object
        new_comment.save()

    else:
        raise Http404

    return HttpResponseRedirect(request.POST.get("next","/"))

@method_decorator(login_required, name="dispatch")
class UpdateCommentView(UpdateView):
    model = Comment
    fields = ("content",)

    def post(self, request, *args, **kwargs):
        comment_post_id = request.POST.get("comment_id", None)
        comment_post_content = request.POST.get("comment_content", None)
        next = request.POST.get("next","/")
        comment_obj = Comment.objects.get(id=comment_post_id)
        comment_author = comment_obj.author

        if comment_post_id and comment_post_content and (comment_author == request.user):
            comment_obj.content = comment_post_content
            comment_obj.save()
            return HttpResponseRedirect(next)

        return HttpResponseRedirect(next)






"""
@login_required
def edit_comment(request):
    this_comment = Comment.objects.get(pk=request.POST.get("id",None))
    comment_content = request.POST.get("comment_content",None)

    if not this_comment.author is request.user:
        return HttpResponseBadRequest
    if not this_comment and not comment_content:
        return HttpResponseBadRequest

    this_comment.content = comment_content
    this_comment.save()

    return JsonResponse(dict(this_comment))
"""



"""
class UpdateCommentView(UpdateView):
    model = Comment
    fields = ("content")

    def get(self, request, *args, **kwargs):

        comment_id = request.GET.get("id",None)
        app_label = request.GET.get("app_label",None)
        model_name = request.GET.get("model_name",None)

        content_type_for_model = ContentType.objects.get(app_label=app_label, model=model_name)
        # app_label - название/имя приложения; model - имя модели.
        # Для большей информации - https://djbook.ru/rel1.9/ref/contrib/contenttypes.html

        this_object = content_type_for_model.get_object_for_this_type(id=comment_id)
        form_content = this_object.content
        context = {"content": form_content}

        return render(request,"comment_templates/comment_form.html",context)
"""


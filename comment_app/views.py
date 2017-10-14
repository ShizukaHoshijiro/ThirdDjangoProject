from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from comment_app.models import Comment
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from comment_app.forms import AddingCommentForm
from django.contrib.contenttypes.models import ContentType,ContentTypeManager
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required
def add_comment(request):

    form = AddingCommentForm(request.POST)
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

        # Получаем текущий объект,
        # get_object_for_this_type - аналог get(), получает объект из выборки всех объектов модели предстовляемой данным экземпляром ContentType
        # Пздц всё сложно.
        this_object = content_type_for_model.get_object_for_this_type(id=object_id)
        # Нерабочая "версия", хз зачем я её оставил.
        # model = ContentType.get_object_for_this_type(content_type_for_model)
        # Возможно, лишняя промежуточная переменная, можно заменить на ContentType.objects.get_for_id()
        # object_set_for_this_model = ContentType.objects.get_for_model(model)
        new_comment = Comment()
        new_comment.content = comment_content
        new_comment.author = request.user
        new_comment.object = this_object
        new_comment.save()

    else:
        raise Http404

    return HttpResponseRedirect(request.POST.get("next","/"))

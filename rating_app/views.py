from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from rating_app.models import Like
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from core.forms import IndexPageForm
from django.contrib.contenttypes.models import ContentType,ContentTypeManager
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Count
import json


@login_required
def add_like(request):

    # data - parsed JSON
    data = json.loads(request.body.decode("utf-8")) # request.body - сырой POST запрос. ".decode("utf-8")" т.к. это сырые байты

    # model_name = request.POST.get("model_name", None)  # Имя модели в, обязательно, нижнем регистре.
    # object_id = request.POST.get("object_id", None)
    # app_label = request.POST.get("app_label", "core")

    model_name = data['model_name']
    object_id = data['object_id']
    app_label = data['app_label']

    if model_name and object_id and app_label:
        content_type_for_model = ContentType.objects.get(app_label=app_label, model=model_name)
        # Экземпляр ContentType'a для данной модели
        this_object = content_type_for_model.get_object_for_this_type(id=object_id)
        # Получаем текущий объект,
        # get_object_for_this_type - аналог get(),
        # получает объект из выборки всех объектов модели предстовляемой данным экземпляром ContentType

        try:
            Like.objects.get(user=request.user, model_type=content_type_for_model, object_id=object_id)
        # Проверяем на исключение "DoesNotExist", потомок "ObjectDoesNotExist",
        # вызываемое в случае если юзер ещё не ставил лайк, т.е.  get(...) возвращает исключение.

        except ObjectDoesNotExist:
            new_like = Like()
            new_like.user = request.user
            new_like.object = this_object
            new_like.save()
        # Создаём новый лайк если его ешё нет.

        else:
            Like.objects.get(user=request.user, model_type=content_type_for_model, object_id=object_id).delete()
        # Удаляем лайк если он есть.
        # this_obj_with_likes = this_object.annotate(num_of_likes =  Count(Like))

        return JsonResponse({"likes":this_object.likes.count()})

    else:
        raise Http404

    # Оно таки работает, шок
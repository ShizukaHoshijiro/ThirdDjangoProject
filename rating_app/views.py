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

@login_required
def add_like(request):

    model_name = request.POST.get("model_name", None)  # Имя модели в, обязательно, нижнем регистре.
    object_id = request.POST.get("object_id", None)
    app_label = request.POST.get("app_label", "core")

    if model_name and object_id:

        content_type_for_model = ContentType.objects.get(app_label=app_label, model=model_name)  # Экземпляр ContentType'a для данной модели
        this_object = content_type_for_model.get_object_for_this_type(id=object_id)

        if Like.object.get(user=request.user, object=this_object):
            Like.object.get(user=request.user, object=this_object).delete()

        else:
            new_like = Like()
            new_like.user = request.user
            new_like.object = this_object
            new_like.save()

    else:
        raise Http404
    return HttpResponseRedirect(request.path)
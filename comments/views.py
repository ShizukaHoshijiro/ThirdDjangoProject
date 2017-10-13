from django.http import HttpResponse, HttpResponseRedirect
from core.models import Topic,Comment
from django.contrib.contenttypes.models import ContentType,ContentTypeManager
from django.http import Http404,JsonResponse
from core.forms import CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def add_comment(request):

    form = CommentForm(request.POST)
    form.is_valid()
    comment_content = form.cleaned_data.get("content",None)

    model_id = request.POST.get("model_id",None) # Id модели
    object_id = request.POST.get("object_id",None) # id(pk) отдельной модели

    if model_id and object_id and comment_content:
        # Получает экземпляр ContentType для текущей модели
        content_type_for_model = ContentType.objects.get(id=model_id)
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

def get_comment(request, model_id, object_id):
    # model_id = request.POST.get("model_id",None) # Id модели
    # object_id = request.POST.get("object_id",None) # id(pk) отдельной модели
    # OLD

    if model_id and object_id:
        comments_for_this_object = Comment.objects.filter(model_type_id=model_id,object_id=object_id)
        comment_dict = {"debugg": "lal"}
        for comment in comments_for_this_object:
            i = 0
            comment_dict[i] = dict(comment)
            i = i + 1
        return JsonResponse(comment_dict, safe=False)
    else:
        return "Not all parameters"
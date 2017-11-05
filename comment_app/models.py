from django.db import models
from django.conf import settings
from django.db.models import PROTECT,CASCADE
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from rating_app.models import Like


class CustomCommentsQuerySet(models.QuerySet):
    def order_by_number_of_likes(self):
        queryset = self.annotate(likes_count=models.Count("likes")).order_by("-likes_count")
        return queryset


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=PROTECT)
    content = models.CharField(max_length=120)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # Позволяет обращатся к списку привязаных like'ов через likes
    # content_type_field="model_type" - имя поля, видимо
    likes = GenericRelation(Like, related_query_name="likes", content_type_field="model_type")

    model_type = models.ForeignKey(ContentType)
    # имя/тип модели, в таблице ContentTypes # Связь с экземпляром ContentType'a
    object_id = models.PositiveIntegerField()
    # id объекта
    object = GenericForeignKey("model_type","object_id")
    # "Соеденяет" model_type и object_id для прямого доступа к объекту

    objects = CustomCommentsQuerySet.as_manager()
    # Custom query set

    class Meta:
        ordering = ("-pub_date",)


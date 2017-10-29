from django.db import models
from django.conf import settings
from django.db.models import PROTECT,CASCADE
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=PROTECT)
    content = models.CharField(max_length=120)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    model_type = models.ForeignKey(ContentType)
    # имя/тип модели, в таблице ContentTypes # Связь с экземпляром ContentType'a
    object_id = models.PositiveIntegerField()
    # id объекта
    object = GenericForeignKey("model_type","object_id")
    # "Соеденяет" model_type и object_id для прямого доступа к объекту

    class Meta:
        ordering = ("-pub_date",)
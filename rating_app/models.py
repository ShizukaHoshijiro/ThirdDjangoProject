from django.db import models
from django.conf import settings
from django.db.models import PROTECT,CASCADE
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation

class Like(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="likes", on_delete=PROTECT)

    model_type = models.ForeignKey(ContentType)    # Связь с экземпляром ContentType'a
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey("model_type","object_id")
    # "Соеденяет" model_type и object_id для прямого доступа к объекту

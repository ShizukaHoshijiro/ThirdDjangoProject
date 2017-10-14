from django.db import models
from django.conf import settings
from django.db.models import PROTECT,CASCADE
from django.contrib.contenttypes.models import ContentType
from comment_app.models import Comment
from django.contrib.contenttypes.fields import GenericRelation

class Topic(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    # settings.AUTH_USER_MODEL - текущий пользователь
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=PROTECT)
    # auto_now_add - Автоматически добавляет значение при создании(не при изменении).
    # auto_now - Автоматически добавляет/изменяет значение при создании/обновлении объекта.
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    # Позволяет обращатся к списку привязаных Comment'ов через comment_app
    # content_type_field="model_type" - имя поля, видимо
    comments = GenericRelation(Comment, related_query_name="comment_app", content_type_field="model_type")

    # Возвращает заголовок как текстовое преобразование/представление.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("core:detail", kwargs={"pk":str(self.id)})

    class Meta:
        # Сортировка по умолчанию, по дате("-" в начале означает обратный порядок) и по заголовку.
        ordering = ("-pub_date","title")

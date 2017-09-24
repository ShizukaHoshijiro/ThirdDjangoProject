from django.db import models
from django.conf import settings

class Topic(models.Model):
    topic_title = models.CharField(max_length=40)
    topic_description = models.TextField()
    # settings.AUTH_USER_MODEL - текущий пользователь
    topic_author = models.ForeignKey(settings.AUTH_USER_MODEL)
    # auto_now_add - Автоматически добавляет значение при создании(не при изменении).
    # auto_now - Автоматически добавляет/изменяет значение при создании/обновлении объекта.
    topic_pub_date = models.DateTimeField(auto_now_add=True)
    topic_update_date = models.DateTimeField(auto_now=True)

    # Возвращает заголовок как текстовое преобразование.
    def __str__(self):
        return self.topic_title

    class Meta:
        # Сортировка по умолчанию, по дате("-" в начале означает обратный порядок) и по заголовку.
        ordering = ("-topic_pub_date","topic_title")
from django.contrib import admin
from comment_app.models import Comment

# Регистрирует модель Topic для администативного сайта по умолчанию.
admin.site.register(Comment)
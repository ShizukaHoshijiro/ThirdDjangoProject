from django.contrib import admin
from core.models import Topic

# Регистрирует модель Topic для администативного сайта по умолчанию.
admin.site.register(Topic)



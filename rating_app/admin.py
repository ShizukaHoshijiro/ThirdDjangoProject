from django.contrib import admin
from rating_app.models import Like

# Регистрирует модель Topic для администативного сайта по умолчанию.
admin.site.register(Like)
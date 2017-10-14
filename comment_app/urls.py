from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login,logout
from .views import add_comment

urlpatterns = [
    url(r"^add/$",add_comment,name="add_comment")
]
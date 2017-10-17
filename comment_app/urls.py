
from django.conf.urls import url, include
from comment_app import views

app_name = "comment_app"
urlpatterns = [
    url(r"^add/$",views.add_comment,name="add_comment"),
]
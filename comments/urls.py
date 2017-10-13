from django.conf.urls import url, include
from comments.views import add_comment,get_comment

app_name = "comments"
urlpatterns = [
    url(r"^add$", add_comment, name="add_comment"),
    url(r"^get/(?P<model_id>\d+)/(?P<object_id>\d+)$", get_comment, name="get_comment")
]
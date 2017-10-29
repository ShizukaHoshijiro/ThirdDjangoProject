
from django.conf.urls import url, include
from rating_app import views

app_name = "rating_app"
urlpatterns = [
    url(r"^add/$",views.add_like,name="add_like"),
]
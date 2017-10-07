from django.conf.urls import url, include
from core import views


app_name = "core"
urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^(?P<pk>\d+)/$", views.Topic_DetailView.as_view(), name="detail"),
    # "\d" - цифры "+" - один или больше  #exp: /21/
    url(r"^create/", views.Topic_CreateView.as_view(), name="create")
]

#url(r"^list/(?P<id>/d+)/$", )
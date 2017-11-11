from django.conf.urls import url, include
from core import views


app_name = "core"
urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^(?P<pk>\d+)/$", views.TopicDetailView.as_view(), name="detail"),
    # "\d" - цифры "+" - один или больше  #exp: /21/
    url(r"^create/", views.TopicCreateView.as_view(), name="create"),
    url(r"^list/(?P<page>\d+)",views.TopicsListView.as_view(), name="list")
]

#url(r"^list/(?P<id>/d+)/$", )
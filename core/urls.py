from django.conf.urls import url, include
from core import views


app_name = "core"
urlpatterns = [
    url(r"^$",views.IndexView.as_view(), name="index"),
    # url(r"^detail/(?P<topic_id>\d+)/$",views. , name="detail"),

]

#url(r"^list/(?P<id>/d+)/$", )
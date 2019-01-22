# blog/urls.py
from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
    url(r'^$', views.post_list),
]

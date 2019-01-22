from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-ㅎㅏ-ㅣ가-힣]{2,3})/(?P<age>\d+)/$', views.hello),
]
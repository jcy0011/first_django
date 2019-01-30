from django.conf.urls import url, include
from django.urls import path

from . import views
from . import views_cbv

app_name='dojo'
urlpatterns=[
    path('new/', views.post_new),
    path('<int:id>/edit/', views.post_edit),
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-ㅎㅏ-ㅣ가-힣]{2,3})/(?P<age>\d+)/$', views.hello),
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^excel/$', views.excel_download),

    url(r'^cbvlist1/$', views_cbv.post_list1),
    url(r'^cbvlist2/$', views_cbv.post_list2),
    url(r'^cbvlist3/$', views_cbv.post_list3),
    url(r'^cbvexcel/$', views_cbv.excel_download),
]

# blog/urls.py
from django.conf.urls import url
from . import views
from django.urls import path
from blog import views

urlpatterns = [
    url(r'^$', views.post_list),
    #url(r'^new/$', views.post_new, name='post_new'),
    #url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='post_delete'),
    #url(r'^(?P<id>\d+)/comments/$', views.comment_list, name='comment_list'),
    #url(r'^(?P<post_id>\d+)/comments/(?P<id>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    #url(r'^(?P<post_id>\d+)/comments/(?P<id>\d+)/delete/$', views.comment_delete, name='comment_delete'),
]

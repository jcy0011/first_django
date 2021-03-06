# blog/urls.py
from django.conf.urls import url, include

from blog import views_cbv
from django.conf.urls.static import static

from . import views
from django.urls import path
from blog import views
from django.conf import settings

app_name='blog'
urlpatterns = [
    url(r'^$', views_cbv.post_list, name='post_list'),
    url(r'^new/$', views.post_new, name='post_new'),
    path('cbv/new/', views_cbv.post_new),
    url(r'^detail/(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),
    url(r'^cbv/(?P<pk>\d+)/edit/$', views_cbv.post_edit),
    url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.post_delete, name='post_delete'),
    #url(r'^(?P<id>\d+)/comments/$', views.comment_list, name='comment_list'),
    #url(r'^(?P<post_id>\d+)/comments/(?P<id>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    #url(r'^(?P<post_id>\d+)/comments/(?P<id>\d+)/delete/$', views.comment_delete, name='comment_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
"""first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, re_path
from django.conf.urls import include, url
def root(request):
    return redirect('blog:post_list')

urlpatterns = [
    path('', lambda r: redirect('blog:post_list'), name='root'),
    path('admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^dojo/', include('dojo.urls', namespace='dojo')),
    path('accounts/', include('accounts.urls')),
    url(r'^shop/', include('shop.urls', namespace='shop'))
]


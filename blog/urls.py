"""
URL patterns for blog app
"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^/tag(?:/(?P<slug>[^\.]+))?$', views.tag, name='tag'),
    url(r'^(?:/(?P<slug>[^\.]+))$', views.post, name='post'),
    url(r'^$', views.blog_home, name='blog'),
]

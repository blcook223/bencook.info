from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^tags(?:/(?P<tag>[\w\-]+))?/$', views.tags, name='tags'),
    url(r'^(?P<short_title>[\w\-]+)/$', views.post, name='post'),
    url(r'^$', views.blog_home, name='blog_home'),
]

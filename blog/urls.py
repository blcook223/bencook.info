from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^tag(?:/(?P<slug>[\d\_\w-]+))?/$', views.tag, name='tag'),
    url(r'^(?P<slug>[\w-\_\d]+)/$', views.post, name='post'),
    url(r'^$', views.blog_home, name='blog'),
]

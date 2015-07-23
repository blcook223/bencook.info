"""bencook_info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
# from django.views.generic.simple import direct_to_template


from bencook_info import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('personal.urls')),
    # url(r'^robots\.txt$', direct_to_template, {
    #     'template': 'robots.txt',
    #     'mimetype': 'text/plain',
    # }),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

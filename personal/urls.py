"""
URL patterns for personal app
"""

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^about$', views.about, name='about'),
]

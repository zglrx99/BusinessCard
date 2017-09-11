from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.myself, name = 'myself'),
    url(r'^experience/$', views.experience, name = 'experience'),
    url(r'^feedback/$', views.feedback, name = 'feedback'),
    url(r'^education/$', views.education, name = 'education'),
]

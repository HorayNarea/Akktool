from django.conf.urls import patterns, url
from akkreditierung import views

urlpatterns = patterns('',
    url(r'^$', views.quorum, name='quorum'),
)

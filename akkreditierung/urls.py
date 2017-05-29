from django.conf.urls import url
from akkreditierung import views

urlpatterns = [
    url(r'^$', views.quorum, name='quorum'),
]

from django.conf.urls import include, url

from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'akktool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(admin.site.urls)),
    url(r'^quorum', include('akkreditierung.urls')),
]

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pastebin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$','manager.views.index'),
    (r'^(?P<id>\d)$','manager.views.get'),
    url(r'^admin/', include(admin.site.urls)),
)

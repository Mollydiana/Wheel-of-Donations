from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'donations.views.home', name='home'),
    url(r'^wheel/', 'donations.views.wheel', name='wheel'),
    url(r'^about/', 'donations.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

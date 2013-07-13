from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from spoticle import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spoticle.views.home', name='home'),
    # url(r'^spoticle/', include('spoticle.foo.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^play/$', views.index, name='play'),
    url(r'^compose/$', views.index, name='compose'),
    url(r'^random/$', views.index, name='random'),
    url(r'^play/(?P<pk>\d+)/$', views.DetailView.as_view(), name='quiz'),
    url(r'^compose/(?P<pk>\d+)/$', views.UpdateView.as_view()),

    url(r'^clip/(?P<clip_id>\d+)/$', views.clip, name='clip'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

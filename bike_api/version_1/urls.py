from django.conf.urls import patterns, url
from bike_api.version_1 import views

urlpatterns = patterns('',
    url(r'^places/$', views.PlacesList.as_view()),
    url(r'^places?afterDate=(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)$', views.PlacesList.as_view()),
    url(r'^routes/$', views.BicycleLinesList.as_view()),
    url(r'^routes?afterDate=(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)$', views.BicycleLinesList.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)
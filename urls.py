from django.conf.urls import patterns, url

from context import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<_uuid>\d+)$', views.beaconInteraction, name='beaconInteraction')


)


from django.conf.urls import patterns, url

urlpatterns = patterns(
	'globalsupply.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^quienes-somos/$', 'about', name="homepageabout"),
	url(r'^contacto/$', 'contact', name="homepagecontact"),
)

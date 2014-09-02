from django.conf.urls import patterns, include, url
from django.conf import settings
from sitemaps import StaticViewSitemap
from django.http import HttpResponse
#from django.conf.urls.i18n import i18n_patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
sitemaps = {
	'pages': StaticViewSitemap,
	}

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'globalsupply.views.home', name='home'),
	url(r'^', include('globalsupply.apps.homepage.urls')),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
	(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
	#Google Web master Tool
	(r'^googlec34fe789f50fc843\.html$', lambda r: HttpResponse("google-site-verification: googlec34fe789f50fc843.html", mimetype="text/plain")),
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
	(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
	(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
	(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
	url(r'^blog/', include('zinnia.urls')),
	(r'^i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
	from django.views.generic import TemplateView
	urlpatterns += patterns(
		'',
		url(r'^404/$', TemplateView.as_view(template_name="404.html")),
		url(r'^403/$', TemplateView.as_view(template_name="403.html")),
		(r'^500/$', TemplateView.as_view(template_name="500.html")),
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
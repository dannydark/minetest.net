from django.conf.urls import patterns, include, url
import minetest.settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'minetest.views.home', name='home'),
	# url(r'^minetest/', include('minetest.foo.urls')),

	url(r'^$', 'main.views.index'),
	url(r'^news$', 'main.views.news'),
	url(r'^download$', 'main.views.download'),
	url(r'^contribute$', 'main.views.contribute'),

	# Old URIs
	url(r'^index.php$', 'main.views.index'),
	url(r'^news.php$', 'main.views.news'),
	url(r'^download.php$', 'main.views.download'),
	url(r'^contribute.php$', 'main.views.contribute'),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),
)

# Serve media directly in DEBUG mode (supposedly running on ./manage.py testserver)
if minetest.settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
				'document_root': minetest.settings.MEDIA_ROOT, 'show_indexes':True}),
	)


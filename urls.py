from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    	(r'^post/$', 'post.views.index'),
	(r'^post/new/$', 'post.views.new'),
	(r'^post/(?P<nid>\d+)/$','post.views.detail'),
	(r'^post/create_note/$', 'post.views.create_note'),
	(r'^post/del_note/(?P<nid>\d+)/$','post.views.delete_note'),
	(r'^post/upd_note/(?P<nid>\d+)/$','post.views.update_note'),
	(r'^post/upd/(?P<nid>\d+)/$','post.views.upd'),
	(r'^admin/', include(admin.site.urls)),
)

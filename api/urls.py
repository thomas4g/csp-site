from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views',
    # Examples:
    # url(r'^$', 'AgencySite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(.*)/', 'api'),

)
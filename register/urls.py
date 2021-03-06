from django.conf.urls import patterns, include, url

urlpatterns = patterns('register.views',
    # Examples:
    # url(r'^$', 'AgencySite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index'),
    url(r'^index/', 'index'),
    url(r'^login/', 'login_view'),
    url(r'^register/', 'register'),
    url(r'^success/', 'thanks'),
    url(r'^welcome/', 'welcome'),
    url(r'^logout/', 'logout_view'),
)
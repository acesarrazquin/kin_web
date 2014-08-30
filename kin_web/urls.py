from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'kin_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'kin_web.views.home', name='main'),
    url(r'^home/$', 'kin_web.views.home', name='home'),
    url(r'^downloads/$', 'kin_web.views.downloads', name='downloads'),
    url(r'^about/$', 'kin_web.views.about', name='about'),
    url(r'^contact/$', 'kin_web.views.contact', name='contact'),
    url(r'^contact/thanks/$', 'kin_web.views.thanks', name='thanks'),


]

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'kin_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'kin_web.views.main', name='main'),
    url(r'^hello/$', 'kin_web.views.hello', name='hello'),
    url(r'^now/$', 'kin_web.views.now', name='now'),
    url(r'^now/plus/(\d{1,2})/$', 'kin_web.views.plus', name='plus'),
    url(r'^metadata/$', 'kin_web.views.meta', name='metadata'),
    url(r'^search-form/$', 'kin_web.views.search_form', name='search-form'),
    url(r'^search/$', 'kin_web.views.search', name='search'),
    url(r'^contact/$', 'kin_web.views.contact', name='contact'),
    url(r'^contact/thanks/$', 'kin_web.views.thanks', name='thanks')
]

from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings #static for css
from django.conf.urls.static import static #static for css
from appone import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView #redirect
from django.core.urlresolvers import reverse #redirect

admin.autodiscover()
urlpatterns = [
    url(r'^',admin.site.urls),
    #url(r'^home/', admin.site.urls),
    #url(r'^jet/', include('jet.urls', 'jet')),
    #url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    # url(r'^stack/',views.appo,name='appone'),
    # url(r'^select2/', include('django_select2.urls)),
    url(r'^newcase/',views.home,name='home'),
]
# urlpatterns += patterns('', (
#     r'^static/(?P<path>.*)$',
#     'django.views.static.serve',
#     {'document_root': settings.STATIC_ROOT}
# ))

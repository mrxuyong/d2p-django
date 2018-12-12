from django.conf.urls import include, url
from django.contrib import admin
import goods.views as gv

urlpatterns = [
    # Examples:
    # url(r'^$', 'd2p.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-token-auth/', 'jwt_auth.views.obtain_jwt_token'),

    url(r'^goods/list/', gv.index),
]

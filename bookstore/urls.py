from django.conf.urls import include, url
from django.contrib import admin
from store.views import index, store

urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^store/', store, name='store'),
    url(r'^admin/', include(admin.site.urls)),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]

urlpatterns += staticfiles_urlpatterns()

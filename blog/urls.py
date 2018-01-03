from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<slug>[-\w\d]+)/delete/$', views.post_delete, name='post_delete'),

    url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),



]

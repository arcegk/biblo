from django.conf.urls import patterns, url

from libros import views

urlpatterns = patterns('',
  url(r'^$', views.libros_list, name='libros_list'),
  url(r'^new$', views.libros_create, name='libros_create'),
  url(r'^edit/(?P<pk>\d+)$', views.libros_update, name='libros_update'),
  url(r'^delete/(?P<pk>\d+)$', views.libros_delete, name='libros_delete'),
)
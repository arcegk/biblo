from django.conf.urls import patterns, url

from .views import *

urlpatterns=patterns('',
	url(r'reserva_registro/$',reserva_registro, name = 'reserva_registro'),
	url(r'reserva_consulta/$',reserva_consulta, name = 'reserva_consulta'),
	url(r'reserva_detalle/(?P<codigo>[0-9]+)/$',reserva_detalle, name = 'reserva_detalle'),
)
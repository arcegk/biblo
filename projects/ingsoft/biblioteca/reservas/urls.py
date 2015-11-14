from django.conf.urls import patterns, url

from reservas.views import *

urlpatterns=patterns('',
	url(r'reserva_registro/$',reserva_registro, name = 'reserva_registro'),
	url(r'reserva_consulta/$',reserva_consulta, name = 'reserva_consulta'),
)
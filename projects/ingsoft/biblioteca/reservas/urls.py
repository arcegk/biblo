from django.conf.urls import patterns, url

from views

urlpatterns=patterns('',
	url(r'reserva_consulta/$',reserva_consulta, name = 'reserva_consulta'),
)
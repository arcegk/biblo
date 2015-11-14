from django.conf.urls import include, url
from pazys.views import GetUser , GenerarPazySalvo , AjxConsulta , ConsultarPazySalvo , AjxGenerar

urlpatterns = [
 	url(r'^get-user/$', GetUser.as_view() , name = "getus"),
    url(r'^generar/$', GenerarPazySalvo.as_view() , name = "gen"),
    url(r'^ajx-consulta/$', AjxConsulta.as_view() , name = "ajxC"),
    url(r'^ajx-generar/$', AjxGenerar.as_view() , name = "ajxC"),
    url(r'^consultar/$', ConsultarPazySalvo.as_view() , name = "gen"),
]
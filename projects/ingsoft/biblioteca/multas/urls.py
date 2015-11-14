from django.conf.urls import include, url
from .views import GenerarDevolucion , AjxGenerarDevolucion , ConsultarMulta , AjxConsultaMulta

urlpatterns = [
    url(r'^ajx-consultar$', AjxConsultaMulta.as_view() , name = "ajxcm"),
    url(r'^ajx-generar$', AjxGenerarDevolucion.as_view() , name = "ajxGm"),
    url(r'^generar/$', GenerarDevolucion.as_view() , name = "gend"),
    url(r'^consultar/$', ConsultarMulta.as_view() , name = "com"),
]
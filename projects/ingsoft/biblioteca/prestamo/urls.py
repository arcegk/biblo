from django.conf.urls import include, url
from .views import AjxConsultaLibro, AjxGenerarPrestamo , AjxConsultaPrestamo , GenerarPrestamo , ConsultarPrestamo

urlpatterns = [
    url(r'^ajx-consultarl$', AjxConsultaLibro.as_view() , name = "ajxcl"),
    url(r'^ajx-generar$', AjxGenerarPrestamo.as_view() , name = "ajxGp"),
    url(r'^ajx-consultarp$', AjxConsultaPrestamo.as_view() , name = "ajxcp"),
    url(r'^generar/$', GenerarPrestamo.as_view() , name = "genp"),
    url(r'^consultar/$', ConsultarPrestamo.as_view() , name = "cop"),
]
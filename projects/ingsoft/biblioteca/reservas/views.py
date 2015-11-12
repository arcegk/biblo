from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def reserva_consulta(request):
    
    return render_to_response('reserva_consulta.html',{},RequestContext(request))
    
    
def reserva_registro(request):
    
    return render_to_response('reserva_registro.html',{},RequestContext(request))
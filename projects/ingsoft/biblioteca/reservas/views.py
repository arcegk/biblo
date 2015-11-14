from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.template.context_processors import csrf

from reservas.models import Reserva
from libros.models import Libro
from pazys.models import Estudiante

@csrf_protect
def reserva_consulta(request):
    if request.method == 'POST':
        codigo=request.POST.get('codigo','')
        reserva = Reserva.objects.get(id=codigo)
        if reserva == None :
            return render_to_response('reserva_consulta.html',{'mensaje':'Reserva no registrada',},RequestContext(request))
        else:
            return render_to_response('reserva_consulta.html',{'reserva':reserva},RequestContext(request))
    return render_to_response('reserva_consulta.html',{},RequestContext(request))
    
@csrf_protect   
def reserva_registro(request):    
    if request.method=='POST':
        accion = request.POST.get("accion", "")        
        if accion == "1":
            codigo = request.POST.get("libro", "")
            libro = Libro.objects.get(id=codigo)
            return render_to_response('reserva_registro.html',{'libro':libro},RequestContext(request))
        elif accion == "2":
            codigo = request.POST.get("libro", "")
            libro = Libro.objects.get(id=codigo)
            cod_estudiante = request.POST.get("estudiante", "")
            estudiante = Estudiante.objects.get(codigo__exact=cod_estudiante)
            return render_to_response('reserva_registro.html',{'libro':libro,'estudiante':estudiante},RequestContext(request))        
        elif accion == "3":
            codigo = request.POST.get("libro", "")
            libro = Libro.objects.get(id=codigo)
            cod_estudiante = request.POST.get("estudiante", "")
            estudiante = Estudiante.objects.get(codigo__exact=cod_estudiante)
            reserva=Reserva(libro=libro,estudiante=estudiante)
            return render_to_response('reserva_registro.html',{'reserva':reserva},RequestContext(request))
    else:
        v={'view_documento':False,'view_libro':False}
        return render_to_response('reserva_registro.html',v,RequestContext(request))
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .forms import ReservaForm
from .models import Reserva

# Create your views here.
def reserva_consulta(request):    
    if request.method=='POST':
        for key in request.POST:
            print(request.POST[key])
        codigo = request.POST.get("txtCodigo", "")
        reserva = Reserva.objects.get(id__exact=codigo)
        if reserva == null :
            return render_to_response('reserva_consulta.html',{'mensaje':'Reserva no registrada'},RequestContext(request))
        else:
            return render_to_response('reserva_consulta.html',{'reserva':reserva},RequestContext(request))
    return render_to_response('reserva_consulta.html',{},RequestContext(request))
    
@csrf_exempt    
def reserva_registro(request):
    
    if request.method=='POST':
        print(request.POST)
        accion = request.POST.get("hdnAccion", "")
        print(accion)
        if accion == "1":
            v={'view_documento':False,'view_libro':False,'libro':'Mi Libro','autor':'Steven','descripcion':'Un libro','material':'Papel','clasificacion':'Accion','isbn':'kdjfsldfjsd'}
            print(v)
            return render_to_response('reserva_registro.html',v,RequestContext(request))
        else:
            v={'view_documento':False,'view_libro':False}
            return render_to_response('reserva_registro.html',v,RequestContext(request))
    else:
        v={'view_documento':False,'view_libro':False}
        return render_to_response('reserva_registro.html',v,RequestContext(request))
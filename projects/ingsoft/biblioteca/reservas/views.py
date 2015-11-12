from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def reserva_consulta(request):
    return render_to_response('reserva_consulta.html',{},RequestContext(request))
    
@csrf_exempt    
def reserva_registro(request):
    v={}
    if request.method == 'POST':        
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
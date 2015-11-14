from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView , View
from django.http import HttpResponse
import json
from .models import Multa , Devolucion
from pazys.models import PazySalvo , Estudiante
from prestamo.models import RegistroPrestamo
from libros.models import Libro 
from datetime import datetime  
from django.utils import timezone



# Create your views here.
class GenerarDevolucion(TemplateView):
	template_name = "multa.html"


class AjxGenerarDevolucion(View):

# faltan validaciones de multas y prestamos

	def get(self, request):

		ide = request.GET.get('id')
		estado = request.GET.get('estado')

		diccionario = []
		try:
			pres = RegistroPrestamo.objects.get(id=ide)
			pres.activo = False
			pres.save()
			dev = Devolucion()
			dev.estado = estado
			dev.prestamof = pres
			dev.fecha = timezone.now()
			dev.save()

			if pres.fechaLimite < dev.fecha:
				mul = Multa()
				mul.estudiante = pres.estudiante 
				mul.libro = pres.libro
				delta = dev.fecha - pres.fechaLimite
				mul.dias_retraso = delta.days
				causa = "Demora en la devolucion"
				mul.valor_total = str(5000*(delta.days))

			if dev.estado.lower() == "malo" or dev.estado.lower() == "regular":
				mul = Multa()
				mul.estudiante = pres.estudiante 
				mul.libro = pres.libro
				mul.dias_retraso = 0
				mul.causa = "Libro en mal estado"
				mul.valor_total = pres.libro.preciocompra

			diccionario.append({"listo" : True})

		except ObjectDoesNotExist:
			pass

		return HttpResponse(json.dumps({'data' : diccionario}) ,content_type='application/json')




class ConsultarMulta(TemplateView):
	template_name = "cm.html"



class AjxConsultaMulta(View):

	def get(self, request):
		code = request.GET['code']
		print code
		diccionario = []
		dic = []
		try :
			estudiante = Estudiante.objects.get(codigo=code)
			dev = Multa.objects.filter(estudiante=estudiante)
			
			for item in dev:	

				dic.append({ 

						'valor' : item.valor_total,
						'causa' : item.causa,
						
					})
			diccionario.append({'nombre' : estudiante.nombre , 'multas' : dic})

		except ObjectDoesNotExist:
			pass

		
		return HttpResponse(json.dumps({'data' : diccionario}) ,content_type='application/json')




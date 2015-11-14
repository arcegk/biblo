from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView , View
from django.http import HttpResponse
import json
from .models import PazySalvo , Estudiante
from multas.models import Multa
from prestamo.models import RegistroPrestamo
from datetime import datetime  



# Create your views here.
class GenerarPazySalvo(TemplateView):
	template_name = "paz.html"


class AjxGenerar(View):

# faltan validaciones de multas y prestamos

	def get(self, request):

		code = request.GET.get('code')
		print code
		diccionario = []
		try:
			est = Estudiante.objects.get(codigo=code)

		except ObjectDoesNotExist:
			pass
		

		q = RegistroPrestamo.objects.filter(estudiante=est, activo=True)
		m = Multa.objects.filter(estudiante=est)

		if m.count() is 0 and q.count() is 0: 
			obj = PazySalvo()
			obj.estudiante = est
			obj.encargado = request.user
			obj.save()
			ide = obj.id 
			print ide
			diccionario.append({
				'id' : ide,
			})
		print diccionario
		

		return HttpResponse(json.dumps({'data' : diccionario}) ,content_type='application/json')




class GetUser(View):


	def get(self, request):
		code = request.GET['code']
		print code
		diccionario = []
		try :
			estudiante = Estudiante.objects.get(codigo=code)
			diccionario.append({ 

					'nombre' : estudiante.nombre,
					'codigo' : estudiante.codigo,

				})
			print diccionario
		except ObjectDoesNotExist:
			pass

		
		return HttpResponse(json.dumps({'data' : diccionario}) ,content_type='application/json')



class ConsultarPazySalvo(TemplateView):
	template_name = "consultar.html"



class AjxConsulta(View):

	def get(self, request):
		code = request.GET['code']
		print code
		diccionario = []
		try :
			estudiante = Estudiante.objects.get(numero_documento=code)
			paz = PazySalvo.objects.filter(estudiante=estudiante)
			
			for pys in paz:	

				diccionario.append({ 

						'nombre' : pys.estudiante.nombre,
						'consecutivo' : pys.id, 
						'encargado' : pys.encargado.username,
						'fecha' : str(pys.fecha_creacion),

					})
			print diccionario
		except ObjectDoesNotExist:
			pass

		
		return HttpResponse(json.dumps({'data' : diccionario}) ,content_type='application/json')




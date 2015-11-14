from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from django.db.models import Q

from libros.models import Libro

class LibroFormAdd(ModelForm):
	class Meta:
		model = Libro
		fields = ['titulo','autor','codigoasignado','temaprincipal', 'temasecundario','editorial','fechapublicacion','dimensiones','estadofisico',
		'estadodebaja','numeropaginas', 'fechacompra', 'cantidad','preciocompra', 'disponibilidad', 'lugarpublicacion','Volumen', 'palabrasclave','descripcionfisica',
		'numeroingreso', 'estadomantenimiento', 'TipodeColeccion', 'ISBN', 'Edicion']
		labels = { 
			'titulo': 'Titulo del libro', 'autor': 'Autores del libro',  'codigoasignado': 'Codigo Asignado', 'temaprincipal': 'Tema principal',
			 'temasecundario': 'Tema secundario', 'editorial': 'Editorial', 'fechapublicacion': 'Fecha de publicacion', 'dimesiones': 'Dimensiones', 'estadofisico': 'Estado Fisico',
			 'estadodebaja': 'Estado de baja', 'numeropaginas': 'Numero de Paginas', 'fechacompra': 'Fecha de Compra', 'cantidad':'Cantidad','preciocompra':'Precio de Compra',
			 'disponibilidad':'Disponibilidad','lugarpublicacion':'Lugar de publicacion', 'Volumen':'Volumen', 'palabrasclave':'Palabras Clave','descripcionfisica':'Descripcion Fisica',
			 'numeroingreso': 'NUmero de Ingreso', 'estadomantenimiento':'Estado de Mantenimiento','TipodeColeccion':'Tipo de Coleccion','ISBN':'Codigo ISBN','Edicion':'Edicion',
		}
		help_texts = {
			'titulo': 'Este es el campo nombre del libro','autor': 'Este es el campo de autor o autores del libro',  'codigoasignado': 'Este es el campo del Codigo Asignado del Libro, se ingresa asi: Codigo decimal Deway (###) Letra # # # , Ejemplo: 008 A 123', 'temaprincipal': 'Este es el campo del Tema principal del libro',
			 'temasecundario': 'Este es el campo del Tema secundario del libro', 'editorial': 'Este es el campo de la Editorial del libro', 'fechapublicacion': 'Este es el campo de la Fecha de publicacion del libro, se ingresa (DD/MM/YYYY)', 'dimesiones': 'Este es el campo de las Dimensiones del libro en centimetros (cm)', 'estadofisico': 'Este es el campo del Estado Fisico del libro, se ingresa (buenascondiciones, malascondiciones, enperdida)',
			 'estadodebaja': 'Este es el campo del Estado de baja, del libro, se ingresa (activo, inactivo)', 'numeropaginas': 'Este es el campo del Numero de Paginas del libro, se ingresan solo numeros', 'fechacompra': 'Este es el campo de la Fecha de Compra del libro, se ingresa (DD/MM/YYYY)', 'cantidad':'Este es el campo de la Cantidad de libros que agrega, se inresan solo numeros','preciocompra':'Este es el campo del Precio de Compra del libro, se ingresan solo numeros',
			 'disponibilidad':'Este es el campo de la Disponibilidad del libro, se ingresa (disponible, nodisponible enreserva, enprestamo)','lugarpublicacion':'Este es el campo del Lugar de publicacion del libro', 'Volumen':'Este es el campo del Volumen del libro, se ingresan solo numeros', 'palabrasclave':'Este es el campo de las Palabras Clave del libro','descripcionfisica':'Este es el campo de la Descripcion Fisica del libro, se ingresan las caracteristicas Fisicas principales del libro, ejemplo: (tipo de portada, material de hojas)',
			 'numeroingreso': 'ESte es el campo del Numero de Ingreso del libro, se ingresan solo libros', 'estadomantenimiento':'Este es el campo de Estado de Mantenimiento del libro, se ingresa (enreposicion, enreparacion), si el libro no obedece a ninguno de estos dos estados ingresa null','TipodeColeccion':'Este es el Tipo de Coleccion a la que pertenece el libro, se ingresa (reserva, general)','ISBN':'Este es el Codigo ISBN del libro, se ingresan solo numeros','Edicion':'Esta es la Edicion del libro',

		}
		error_messages = {
			'titulo': {
				'required': "El campo libro es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
             'autor': {
				'required': "El campo autor es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},

				
				'codigoasignado': {
				'required': "El campo codigoasignado es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'temaprincipal': {
				'required': "El campo temaprincipal es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'temasecundario': {
				'required': "El campo temasecundario es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'editorial': {
				'required': "El campo editorial es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'fechapublicacion': {
				'required': "El campo fechapublicacion es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'dimensiones': {
				'required': "El campo dimensiones es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'estadofisico': {
				'required': "El campo estadofisico es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'estadodebaja': {
				'required': "El campo estadodebaja es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
					
				'numeropaginas': {
				'required': "El campo numeropaginas es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
					
				'fechacompra': {
				'required': "El campo fechacompra es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'preciocompra': {
				'required': "El campo preciocompra es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'disponibilidad': {
				'required': "El campo disponibilidad es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'lugarpublicacion': {
				'required': "El campo lugarpublicacion es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'Volumen': {
				'required': "El campo Volumen es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'palabrasclave': {
				'required': "El campo palabrasclave es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'descripcionfisica': {
				'required': "El campo descripcionfisica es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'numeroingreso': {
				'required': "El campo numeroingreso es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'estadomantenimiento': {
				'required': "El campo estadomantenimiento es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},
				
				'TipodeColeccion': {
				'required': "El campo TipodeColeccion es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},

				'ISBN': {
				'required': "El campo ISBN es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},

				
				'Edicion': {
				'required': "El campo Edicion es obligatorio.",
				#'max_length': _("This writer's name is too long."),
				},


			},
 		

class LibroFormEdit(ModelForm):
	class Meta:
		model = Libro
		fields = ['titulo', 'autor']

def libros_list(request):
	
	try:
		libros = Libro.objects.filter(ISBN=request.GET.get('filter'))
		#libros = Libro.objects.filter(nombre=request.GET['filter'])
	except ObjectDoesNotExist: 
	   # libros = Libro.objects.all()
	   pass

	#if request.GET.has_key("filter"):
	#if( hasattr(request.GET, 'filter') ):
		# request.GET['filter'] != ''        
	#else:
		#libros = Libro.objects.all()
	
	data = {}
	data['libros'] = libros
	return render(request, 'libros/libros_list.html', data)

def libros_create(request):
	form = LibroFormAdd(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('libros:libros_list')
	return render(request, 'libros/libros_form.html', {'form':form})

def libros_update(request, pk):
	libro= get_object_or_404(Libro, pk=pk)
	form = LibroFormEdit(request.POST or None, instance=libro)
	if form.is_valid():
		form.save()
		return redirect('libros:libros_list')
	return render(request, 'libros/libros_form.html', {'form':form})

def libros_delete(request, pk):
	libro= get_object_or_404(Libro, pk=pk)    
	if request.method=='POST':
		libro.delete()
		return redirect('libros:libros_list')
	return render(request, 'libros/libros_confirm_delete.html', {'libro':libro})

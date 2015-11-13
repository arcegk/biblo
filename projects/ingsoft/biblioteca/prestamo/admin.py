from django.contrib import admin
from .models import Libro
from .models import RegistroPrestamo

admin.site.register(Libro)
admin.site.register(RegistroPrestamo)
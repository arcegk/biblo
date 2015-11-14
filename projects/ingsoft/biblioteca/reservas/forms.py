from django.forms import ModelForm
from .models import Reserva

class ReservaForm(ModelForm):
	
	class Meta:
		model=Reserva
		exclude=[]

class ReservaQueryForm(ModelForm):
    pass

    class Meta:
        model = Reserva
        # include all fields you're saving from the form here
        fields = ['id'] 
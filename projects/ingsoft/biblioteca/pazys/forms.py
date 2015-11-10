from django.forms import ModelForm
from .models import Pazy


class CreatePazy(ModelForm):
	Model = Pazy
	fields = "__"
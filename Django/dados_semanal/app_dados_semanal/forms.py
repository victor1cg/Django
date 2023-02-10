from django.forms import ModelForm
from .models import Semanal

class SemanalForm(ModelForm):
    class Meta:
        model = Semanal
        fields = '__all__'
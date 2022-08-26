from .models import Sala
from django.forms import ModelForm


class SalaForm(ModelForm):
    class Meta:
        model = Sala
        fields = ["nome", "capacidade"]

from .models import Phones
from django.forms import ModelForm, TextInput


class PhonesForm(ModelForm):
    class Meta:
        model = Phones
        fields = ["name", "surname", "number"]
        widgets = {
            "name": TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Введите имя',
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию',
            }),
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер',
            }),
        }
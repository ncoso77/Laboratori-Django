from django import forms
from django.contrib.auth.models import User
from models import *
from django.forms import ModelForm
 
 
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }


class CreateForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['habitacio', 'data_ent', 'data_sort']


class EditForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['habitacio', 'data_ent', 'data_sort', 'confirmada', 'qualificacio', 'comentari_qualificacio']
        widgets = {
            'confirmada': forms.CheckboxInput(),
        }

        
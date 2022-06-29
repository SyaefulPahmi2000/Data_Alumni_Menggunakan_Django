from django.forms import ModelForm
from django import forms
from .models import Data_Alumni

class DataForm(ModelForm):
    class Meta:
        model = Data_Alumni
        fields = '__all__'
        Widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
            'pekerjaan' : forms.TextInput({'class':'form-control'}),
            'no_hp' : forms.TextInput({'class':'form-control'}),
            'jenis_kelamin' : forms.Select({'class':'form-control'}),
            'angkatan' : forms.TextInput({'class':'form-control'}),
        }
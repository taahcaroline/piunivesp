from django import forms
from .models import Cadastrovagas



class CadastrovagasForm(forms.ModelForm):
    class Meta:
     model = Cadastrovagas
     fields = '__all__'
    #  widgets = {
    # #         'modelo': forms.Select(attrs={'class': 'form-control'})
    #  }

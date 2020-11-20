from django import forms
from django.core.exceptions import ValidationError
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model  = Pizza
        fields = '__all__'
        
    def clean_description(self):
        desc = self.cleaned_data['description']
        max  = 400
        if len(desc) > max:
            raise ValidationError(f'Descrição deve ter menos que {max} caracteres, vai com calma!')
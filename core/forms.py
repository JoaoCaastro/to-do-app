from .models import To_doModel
from django.forms import DateInput, ModelForm 

class toDoFormModel(ModelForm):
    class Meta:
        model = To_doModel
        fields = '__all__'
        widgets = {
            'startDate': DateInput(
            attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy', 'class': 'form-control'}
            ),
            'endDate': DateInput(
            attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy', 'class': 'form-control'}
            )
        }
    
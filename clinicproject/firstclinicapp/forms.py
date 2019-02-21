from django import forms
from .models import Patient

class RegisterPatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = ("first_name", 'last_name', 'gender', 'date_of_birth', 'notes')

class SearchForm(forms.Form):
    search_id = forms.IntegerField()
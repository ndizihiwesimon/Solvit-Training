from django import forms
from .models import Trainee

class TraineeForm(forms.Form):
    full_name = forms.CharField(required=True)
    dob = forms.DateField(required=True, widget=forms.DateInput())
    
    def save(self):
        pass

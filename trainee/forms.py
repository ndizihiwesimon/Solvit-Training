from django import forms
from .models import Trainee

class TraineeForm(forms.Form):
    full_name = forms.CharField(required=True)
    dob = forms.DateField(required=True, widget=forms.DateInput())
    
    def validate_full_name(self, value):
        try:
            Trainee.objects.get(full_name=value)
            raise forms.ValidationError("This name is already in use")
        except Trainee.DoesNotExist:
            return value
    
    def save(self, validated_data):
        tr = Trainee(full_name=validated_data['full_name'], dob=validated_data['dob'])
        tr.save()

from django import forms
from .models import Trainee


class TraineeForm(forms.Form):
    full_name = forms.CharField(label="Full name", required=True)
    dob = forms.DateField(label="Date of Birth",
                          required=True, widget=forms.DateInput())

    def clean_full_name(self):
        try:
            full_name = self.cleaned_data['full_name']
            Trainee.objects.get(full_name=full_name)
            raise forms.ValidationError("This name is already in use")
        except Trainee.DoesNotExist:
            return self.cleaned_data['full_name']

    def save(self):
        new_trainee = Trainee.objects.create(
            full_name=self.cleaned_data['full_name'], dob=self.cleaned_data['dob'])
        return new_trainee

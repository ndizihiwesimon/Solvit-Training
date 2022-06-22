from django.shortcuts import render
from trainee.forms import TraineeForm

from trainee.models import Trainee

# Create your views here.

def trainees_list(request):
    trainees = Trainee.objects.all()
    
    if request.method == 'POST':
        form = TraineeForm()
        trainee_form = form(request.POST)
        if trainee_form.is_valid():
            trainee_form.save()
        else:
            context = {
                "trainees": trainees,
                "form": trainee_form.errors,
            }
            return render(request, 'trainees/list.html', context)

    
# Listing
# adding -- using forms, modelForms, or forms

# Editing -- View and template only
# Deleting -- View and template only
# Last one -- Login Template

# create 5 views
# 1) listing all trainees
# 2) adding a trainee (Forms)
# 3) editing a trainee  NB on the view and the template
# 4) deleting a trainee NB on the view and the template
# 5) login template
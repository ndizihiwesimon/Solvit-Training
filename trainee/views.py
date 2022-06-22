from django.shortcuts import render
from trainee.forms import TraineeForm

from trainee.models import Trainee

# Create your views here.

def trainees_list(request):
    trainees = Trainee.objects.all()
    context = {
        "trainees": trainees,
    }
    
    if request.method == 'POST':
        form = TraineeForm()
        trainee_form = form(request.POST)
        if trainee_form.is_valid():
            trainee_form.save()
    else:
        return render(request, 'trainees/list.html', context)

    

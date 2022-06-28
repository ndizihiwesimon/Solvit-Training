from django.shortcuts import redirect, render
from trainee.forms import TraineeForm

from trainee.models import Trainee

# Create your views here.

# 1) listing all trainees


def trainees_list(request):
    trainees = Trainee.objects.all()
    context = {
        "trainees": trainees,
    }
    return render(request, 'trainees/list.html', context)

# 2) adding a trainee (Forms)


def create_trainee(request):
    form = TraineeForm()
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainees-list')
        else:
            form = TraineeForm()
    return render(request, 'trainees/create.html', {'form': form})

# 3) editing a trainee  NB on the view and the template


def trainees_update(request):
    if request.method == 'PUT':
        pass

# 4) deleting a trainee NB on the view and the template


def trainees_delete(request):
    pass

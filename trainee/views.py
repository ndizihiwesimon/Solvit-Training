from django.shortcuts import render

from trainee.models import Trainee

# Create your views here.

def trainees_list(request):
    trainees = Trainee.objects.all()
    context = {
        "trainees": trainees,
    }
    return render(request, 'trainees/list.html', context)

from django.shortcuts import render

# Create your views here.
from Evaluation.forms import UserForm
from Evaluation.models import Unit


def add_employee(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        unit = Unit.objects.filter(unit_number=request.POST.unit)[0]
        unit.employee_catalogue.add_employee(request.POST.role, user_form)
    else:
        user_form = UserForm()
    return render(request, 'master/add_employee.html', {'form': user_form})


def show_master_page(request):
    return render(request, 'master/master.html')

from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class SystemUser(User):
    personal_code = models.PositiveIntegerField(primary_key=True, verbose_name='کد-پرسنلی')
    pass


class Employee(SystemUser):
    pass


class Master(SystemUser):
    pass


class Manager(Employee):
    pass


class NormalEmployee(Employee):
    pass


class EmployeeCatalogue(models.Model):
    unit_employees = []

    def add_employee(self, role, user_form):
        if user_form.is_valid():
            if role == "Manager":
                new_employee = Manager(**user_form.cleaned_data)
            else:
                new_employee = NormalEmployee(**user_form.cleaned_data)
            new_employee.save()
            self.unit_employees.append(new_employee)
        else:
            pass


class Unit(models.Model):
    employee_catalogue = models.OneToOneField(EmployeeCatalogue, on_delete=models.CASCADE)
    unit_number = models.PositiveIntegerField(primary_key=True,verbose_name='شماره-واحد')


from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    personal_code = models.PositiveIntegerField(max_length=100, primary_key=True, verbose_name='کاربر')


class Employee(User):
    pass
class Master(User):
    pass

class Manager(Employee):
    pass


class NormalEmployee(Employee):
    pass


class EmployeeCatalogue(models.Model):


    def add_employee(self, role, unit, user_form):
        new_employee = None
        if role == "Manager":
            new_employee = Manager()
        else:
            new_employee = NormalEmployee()
        self.unit_employees.append(new_employee)


class Unit(models.Model):
    employee_catalogue = models.OneToOneField(EmployeeCatalogue,
        on_delete=models.CASCADE,
        )

from django.contrib import admin

# Register your models here.
from Evaluation.models import *
admin.site.register(Manager)
admin.site.register(Unit)
admin.site.register(Employee)
admin.site.register(EmployeeCatalogue)
admin.site.register(SystemUser)
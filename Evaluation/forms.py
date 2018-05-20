
from django import forms

from Evaluation.models import SystemUser


class UserForm(forms.ModelForm):
    class Meta:
        model = SystemUser
        fields = ['personal_code', 'password', 'first_name', 'last_name']
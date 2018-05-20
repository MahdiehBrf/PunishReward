
from django import forms

from Evaluation.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['personal_code', 'password', 'first_name', 'last_name']
from django import forms
from django.contrib.auth.models import User
from . import models


class PatientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['gender', 'age', 'bloodgroup', 'disease', 'address', 'city', 'nic', 'reg_date', 'doctorname',
                  'mobile', 'profile_pic']

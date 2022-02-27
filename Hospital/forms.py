from django import forms
from django.contrib.auth.models import User

from . import models



class HospitalForm(forms.ModelForm):
    class Meta:
        model = models.Hospital

        fields = ['website', 'city', 'email_id',
                  'phone', 'patient', 'address', 'name','profile_pic']


class HospitalUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }



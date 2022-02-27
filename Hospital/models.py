from django.contrib.auth.models import User
from django.db import models
from patient.models import Patient


class Hospital(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Patient/', null=True, blank=True)
    name = models.CharField(max_length=20)
    phone = models.PositiveIntegerField()
    email_id = models.EmailField(max_length=50)
    website = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)

    @property
    #def get_name(self):
     #   return self.user.first_name + " " + self.user.last_name

    #@property
    #def get_instance(self):
     #   return self

    def __str__(self):
        return self.user.first_name

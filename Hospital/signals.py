from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Patient, Hospital


@receiver(post_save,sender=Hospital)
def create_patient(sender,instance,created,**kwargs):
   if created:
        Patient.objects.create(hospital=instance)

@receiver(post_save,sender=Hospital)
def save_patient(sender,instance,**kwargs):
    instance.patient.save()

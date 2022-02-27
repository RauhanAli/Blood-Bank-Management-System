from django.contrib import admin

# Register your models here.
from Hospital.models import Hospital
from donor.models import Donor

admin.site.register(Donor)
admin.site.register(Hospital)
from django.contrib import admin
from .models import *

admin.site.register(Appointment)

class appointmentAdmin(admin.ModelAdmin):
    fields = ['date', 'client_name', 'message']
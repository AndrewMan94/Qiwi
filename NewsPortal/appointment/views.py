from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import mail_admins
from datetime import datetime
from .models import Appointment


class AppointmentView(View):
    def get(self, request):
        return render(request, 'make_appointment.html', {})

    def post(self, request):
        appointment = Appointment(
            date=datetime.strptime(request.POST ['date'], '%Y-%m-%d'),
            client_name=request.POST ['client_name'],
            message=request.POST ['message'],
        )
        appointment.save()

        mail_admins(
            subject=f'{appointment.client_name} {appointment.date.strftime("%d %m %Y")}',
            message=appointment.message,
        )

        return redirect('appointments:make_appointment')
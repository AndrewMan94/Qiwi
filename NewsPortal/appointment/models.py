from django.core.mail import mail_managers
from django.db import models
from datetime import datetime

from django.db.models.signals import post_delete
from django.dispatch import receiver


class Appointment(models.Model):
    date = models.DateTimeField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=200
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'


@receiver(post_delete, sender=Appointment)
def notify_managers_appointment_canceled(sender, instance, **kwargs):
    subject = f'{instance.client_name} has canceled his appointment!'
    mail_managers(
        subject=subject,
        message=f'Canceled appointment for {instance.date.strftime("%d %m %Y")}',
    )

    print(subject)
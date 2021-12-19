from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from .models import PostCategory, CategorySubscribers
from django.template.loader import render_to_string


@receiver(post_save, sender=PostCategory)
def notify_managers_appointment(sender, instance, created, **kwargs):
    subscribers = CategorySubscribers.objects.filter(id_category=instance.id_category)
    for subscriber in subscribers:
        user = subscriber.id_user

        subject = ''
        if created:
            subject = f'Здравствуй, {user}! В категории "{instance.id_category}" создана новая новость!'

        post = instance.id_post
        html_content = render_to_string('add_post_for_subscribers.html', {'post': post, })
        msg = EmailMultiAlternatives(
            subject=subject,
            body='',
            from_email='ManAndEvg@yandex.ru',
            to=[user.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
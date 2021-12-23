from celery import shared_task
import time
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from NewsPortal.BreakingNews.models import CategorySubscribers
from Qiwi.NewsPortal.BreakingNews.models import Post


@shared_task
def new_post_notification(subj, email, content):
    time.sleep(5)

    msg = EmailMultiAlternatives(
        subject=subj,
        body='',
        from_email='ManAndEvg@yandex.ru',
        to=[email],
    )
    msg.attach_alternative(content, "text/html")
    msg.send()

@shared_task()
def weekly_notification():
    print("----------------------------------------------------------------------------------------------------------------------")
    if CategorySubscribers.objects.all().exists():
        subscribers = CategorySubscribers.objects.all()
        for subscriber in subscribers:
            user = subscriber.id_user
            print(user)
            subject = f'Здравствуй, {user}! Еженедельная рассылка новостей по категории "{subscriber.id_category}"'

            post_list = Post.objects.filter(created__gte=(datetime.today() - timedelta(days=7)), id_post_category=subscriber.id_category.pk)
            for post in post_list:
                print(post.title, post.created, subscriber.id_category)

            html_content = render_to_string('New_add_post.html', {'post_list': post_list, })
            msg = EmailMultiAlternatives(
                subject=subject,
                body='',
                from_email='ManAndEvg@yandex.ru',
                to=[user.email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()



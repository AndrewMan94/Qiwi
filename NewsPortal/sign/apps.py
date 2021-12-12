from django.apps import AppConfig


class SignConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sign'


def get_model(param, param1):
    return None
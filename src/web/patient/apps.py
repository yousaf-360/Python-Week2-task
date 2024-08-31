from django.apps import AppConfig
from django.contrib.auth import authenticate


class PatientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web.patient'
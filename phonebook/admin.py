from django.contrib import admin

from .models import Group, PhoneBookContact

# Register your models here.

models_to_register = [
    Group, PhoneBookContact
]


def register_models(models):
    for model in models:
        admin.site.register(model)

register_models(models_to_register)

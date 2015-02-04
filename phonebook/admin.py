from django.contrib import admin

from .models import Group, PhoneBookContact

from base.admin import PhoneBookBaseAdmin

# Register your models here.

models_to_register = [
    Group, PhoneBookContact
]

class GroupAdmin(PhoneBookBaseAdmin):
  list_display = ('id', 'name', 'description', 'created_by')

class PhoneBookContactAdmin(PhoneBookBaseAdmin):
  list_display = ('id', 'name', 'phone_number', 'created_by')


def register_models(models):
  for model in models:
    admin.site.register(model)

# register_models(models_to_register)

admin.site.register(Group, GroupAdmin)
admin.site.register(PhoneBookContact, PhoneBookContactAdmin)

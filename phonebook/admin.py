from django.contrib import admin

from .models import Group, PhoneBookContact, GroupMember

from base.admin import PhoneBookBaseAdmin

# Register your models here.

class GroupAdmin(PhoneBookBaseAdmin):
  list_display = ('id', 'name', 'description', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

class PhoneBookContactAdmin(PhoneBookBaseAdmin):
  list_display = ('id', 'name', 'phone_number', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

class GroupMembersAdmin(PhoneBookBaseAdmin):
  list_display = ('id', 'group', 'member', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

models_to_register = [
  {'model_name': Group, 'model_admin': GroupAdmin},
  {'model_name': PhoneBookContact, 'model_admin': PhoneBookContactAdmin},
  {'model_name': GroupMember, 'model_admin': GroupMembersAdmin},
]


def register_models(models):
  for model in models:
    admin.site.register(model['model_name'], model['model_admin'])

register_models(models_to_register)

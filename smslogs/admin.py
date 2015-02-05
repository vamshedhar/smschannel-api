from django.contrib import admin

from .models import GroupMessage, SingleMessage

from base.admin import SMSBaseAdmin

# Register your models here.

class GroupMessageAdmin(SMSBaseAdmin):
  list_display = ('id', 'sent_to', 'message', 'sent_by', 'sent_on', 'delivery_status', 'created', 'modified')

class SingleMessageAdmin(SMSBaseAdmin):
  list_display = ('id', 'sent_to', 'message', 'sent_by', 'sent_on', 'delivery_status', 'created', 'modified')

models_to_register = [
  {'model_name': GroupMessage, 'model_admin': GroupMessageAdmin},
  {'model_name': SingleMessage, 'model_admin': SingleMessageAdmin},
]


def register_models(models):
  for model in models:
    admin.site.register(model['model_name'], model['model_admin'])

register_models(models_to_register)

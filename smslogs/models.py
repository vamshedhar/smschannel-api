from django.db import models
from model_utils import FieldTracker
from django.conf import settings

from base.models import SMSBaseModel
from phonebook.models import PhoneBookContact, Group

# Create your models here.

class GroupMessage(models.Model):
  tracker = FieldTracker()
  sent_to = models.ForeignKey(_('Group Name'), Group, null=False, related_name='messages')
  message = models.TextField(_('Message'), blank="False")

class SingleMessage(models.Model):
  tracker = FieldTracker()
  sent_to = models.ForeignKey(_('Sent to'), PhoneBookContact, null=False, related_name='messages')
  message = models.TextField(_('Message'), blank="False")

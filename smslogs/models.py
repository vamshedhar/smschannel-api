from django.db import models
from model_utils import FieldTracker
from django.conf import settings

from base.models import SMSBaseModel
from phonebook.models import PhoneBookContact, Group

# Create your models here.

class GroupMessage(SMSBaseModel):
  tracker = FieldTracker()
  sent_to = models.ForeignKey(Group, null=False, related_name='messages')
  message = models.TextField("Message", blank="False")

class SingleMessage(SMSBaseModel):
  tracker = FieldTracker()
  sent_to = models.ForeignKey(PhoneBookContact, null=False, related_name='messages')
  message = models.TextField("Message", blank="False")

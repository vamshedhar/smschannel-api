from django.db import models
from model_utils import FieldTracker
from django.conf import settings

from base.models import PhoneBookBaseModel

# Create your models here.

class Group(PhoneBookBaseModel):
  tracker = FieldTracker()
  name = models.CharField("Group Name", max_length=100, null=False, blank=False)
  description = models.TextField("Description", blank=True)
  head = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='head_of')
  authorized_users = models.ManyToManyField(settings.AUTH_USER_MODEL, null=False, related_name='privileges', help_text='Users who are allowed to send sms to the group.')

class PhoneBookContact(PhoneBookBaseModel):

  MEMBER_TYPE = (
    ('SD', 'Student'),
    ('FA', 'Faculty'),
    ('SF', 'Staff')
  )

  tracker = FieldTracker()
  name = models.CharField("Name", max_length=100, null=False, blank=False)
  phone_number = models.CharField("Phone No.", max_length="15", null=False, blank=False, unique=True)
  type = models.CharField("Contact Type", max_length=10, choices=MEMBER_TYPE, null=False, blank=False)
  groups = models.ManyToManyField(Group, related_name='members')

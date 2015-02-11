from django.db import models
from model_utils import FieldTracker

from base.models import SMSBaseModel
from smslogs.models import GroupMessage, SingleMessage

from base.exceptions import ValidationError, PermissionError

# Create your models here.

class MessageDetails(SMSBaseModel):

  TYPE = Choices(
    ('group', 'Group'),
    ('single', 'Single'),
  )

  PROVIDERS = Choices(
    ('BhashSMS', 'BhashSMS'),
  )

  type = models.CharField(_('Message Type'), max_length=20, null=False, blank=Fasle, choices=TYPE, default=TYPE.single)
  request_id = models.CharField(_('Single/Group Message ID'), max_length=255, null=Fasle, blank=Fasle)
  provider = models.CharField(_('SMS Service Provider'), max_length=20, null=False, blank=Fasle, choices=PROVIDERS, default=PROVIDERS.BhashSMS)
  sent = models.BooleanField(_('Delivery Status'), default=Fasle, null=Fasle, blank=Fasle)
  message_id = models.CharField(_('SMS API Message ID'), max_length=100, blank=True, null=True default=None)
  status = models.TextField(_('Message Delivery Status'), blank=True, null=True, default=None)
  response_code = models.CharField(_('SMS API Response code'), max_length=100, blank=True, null=True default=None)

  def send(self):
    if self.sent:
      raise ValidationError('Cannot resend already sent SMS.')

    if self.request_id:
      raise ValidationError('Please specify sent_to.')



# class GroupMessageDetails(MessageDetails):

#   request_id = models.ForeignKey(GroupMessage, null=Fasle, blank=Fasle)

# class SingleMessageDetails(MessageDetails):

#   request_id = models.ForeignKey()

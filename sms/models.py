from django.db import models
from django.utils.translation import ugettext as _
from model_utils import FieldTracker, Choices

from base.models import SMSBaseModel
from smslogs.models import GroupMessage, SingleMessage

from base.exceptions import ValidationError, PermissionError
import integrations

# Create your models here.

INTEGRATION_MAP = {
    'BhashSMS': integrations.BhashSMSIntegration
}

class MessageDetails(SMSBaseModel):

  TYPE = Choices(
    ('group', 'Group'),
    ('single', 'Single'),
  )

  PROVIDERS = Choices(
    ('BhashSMS', 'BhashSMS'),
  )

  type = models.CharField(_('Message Type'), max_length=20, null=False, blank=False, choices=TYPE, default=TYPE.single)
  request_id = models.CharField(_('Single/Group Message ID'), max_length=255, null=False, blank=False)
  sent_to = models.CharField(_('Single/Group ID'), max_length=255, null=False, blank=False)
  number_list = models.TextField(_('Numbers list'), blank=True, null=True, default=None)
  provider = models.CharField(_('SMS Service Provider'), max_length=20, null=False, blank=False, choices=PROVIDERS, default=PROVIDERS.BhashSMS)
  message_ids = models.TextField(_('SMS API Message IDs'), blank=True, null=True, default=None)
  sent = models.BooleanField(_('Delivery Status'), default=False, null=False, blank=False)
  status_list = models.TextField(_('Message Delivery Status'), blank=True, null=True, default=None)
  response_code = models.CharField(_('SMS API Response code'), max_length=100, blank=True, null=True, default=None)

  def send(self, message):
    if self.sent:
      raise ValidationError('Cannot resend already sent SMS.')

    if self.request_id:
      raise ValidationError('Please specify sent_to.')

    api_integration = INTEGRATION_MAP.get(self.provider)

    API = api_integration(message)
    message = API.send()

    return message



# class GroupMessageDetails(MessageDetails):

#   request_id = models.ForeignKey(GroupMessage, null=False, blank=False)

# class SingleMessageDetails(MessageDetails):

#   request_id = models.ForeignKey()

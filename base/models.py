from django.db import models
from django.conf import settings

from uuidfield import UUIDField
from django_extensions.db.models import TimeStampedModel

from base.exceptions import ValidationError, PermissionError

import arrow

# Create your models here.

class UUIDModel(TimeStampedModel):
  id = UUIDField(primary_key=True, auto=True, editable=False)

  class Meta:
    abstract = True

  def __unicode__(self):
    try:
      return self.name
    except AttributeError:
      return unicode(self.id)

class PhoneBookBaseModel(UUIDModel):
  created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, editable=False, related_name="%(app_label)s_%(class)s_created")
  modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, editable=True, related_name="%(app_label)s_%(class)s_modified")
  deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, editable=True, related_name="%(app_label)s_%(class)s_deleted")

  class Meta:
    abstract = True

  def save(self, *args, **kwargs):
    if self.deleted_by:
      raise ValidationError('You can\'t change deleted_by User')
    if not self.id:
      if not self.created_by:
        raise ValidationError('Please specify created_by User')
      self.modified_by = self.created_by
    return super(PhoneBookBaseModel, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
    if self.id:
      if self.deleted_by is None:
        raise ValidationError('Please specify deleted_by User')
      if self.tracker.changed().get('deleted_by_id', {}) is None:
        self.modified = arrow.now().datetime
        return super(PhoneBookBaseModel, self).save()
      raise ValidationError({'__all__': 'This object has been deleted'})
    else:
      return super(PhoneBookBaseModel, self).delete(*args, **kwargs)


class SMSBaseModel(UUIDModel):

  DELIVERY_STATUS = (
    (1, 'Success'),
    (0, 'Failure')
  )

  sent_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, editable=False, related_name="%(app_label)s_%(class)s_sent")
  sent_on = models.DateTimeField(auto_now_add=True)
  delivery_status = models.IntegerField(max_length=1, choices=DELIVERY_STATUS, default=0)

  class Meta:
      abstract = True

  def save(self, *args, **kwargs):
    if not self.id and not self.sent_by:
      raise ValidationError('Please specify sent_by User')
    if self.id:
      if self.tracker.has_changed('message'):
        raise PermissionError('You cannot change message content.')
      if self.tracker.changed().get('sent_to_id', None) is None:
        super(SMSBaseModel, self).save(*args, **kwargs)
      else:
        raise PermissionError('You cannot change sent_to.')
    return super(SMSBaseModel, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
    raise ValidationError('You cannot delete SMS logs.')

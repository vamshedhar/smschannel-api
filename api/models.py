from django.db import models
from django.conf import settings

# Create your models here.

class Group(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	description = models.TextField(blank=True)
	head = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='head_of')

	def __unicode__(self):
		return self.name

class PhoneBookLog(models.Model):

	MEMBER_TYPE = (
		('SD', 'Student'),
		('FA', 'Faculty'),
		('SF', 'Staff')
	)

	name = models.CharField(max_length=100, null=False, blank=False)
	phone_number = models.BigIntegerField(unique=True)
	member_type = models.CharField(max_length=10, choices=MEMBER_TYPE, null=False, blank=False)
	added_by = models.ForeignKey(settings.AUTH_USER_MODEL)
	added_on = models.DateField(auto_now_add=True)
	groups = models.ManyToManyField(Group, related_name='members')
	active = models.BooleanField(default=True, help_text='Designates if entries are active(True) or deleted(False)')

	def __unicode__(self):
		return self.name

class UserPrivileges(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, related_name='privileges')
	privileges = models.ManyToManyField(Group, null=True, related_name='privileged_users')

	def __unicode__(self):
		return unicode(self.user)

class GroupMessageLog(models.Model):

	DELIVERY_STATUS = (
		(1, 'Success'),
		(0, 'Failure')
	)

	sent_by = models.ForeignKey(settings.AUTH_USER_MODEL)
	sent_to = models.ForeignKey(Group)
	sent_on = models.DateTimeField(auto_now_add=True)
	message = models.TextField()
	delivery_status = models.IntegerField(max_length=1, choices=DELIVERY_STATUS)

	def __unicode__(self):
		return unicode(self.sent_to) + ": " + self.message

class SingleMessageLog(models.Model):

	DELIVERY_STATUS = (
		(1, 'Success'),
		(0, 'Failure')
	)

	sent_by = models.ForeignKey(settings.AUTH_USER_MODEL)
	sent_to = models.ForeignKey(PhoneBookLog)
	sent_on = models.DateTimeField(auto_now_add=True)
	message = models.TextField()
	delivery_status = models.IntegerField(max_length=1, choices=DELIVERY_STATUS)

	def __unicode__(self):
		return unicode(self.sent_to) + ": " + self.message
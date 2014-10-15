from django.db import models
from django.conf import settings

# Create your models here.

class Group(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

class PhoneBook(models.Model):

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

	def __unicode__(self):
		return self.name
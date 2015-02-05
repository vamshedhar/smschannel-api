from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from managers import CustomUserManager

from base.models import UUIDModel

"""
Contains custom user model
"""

class User(AbstractBaseUser, UUIDModel, PermissionsMixin):
	phone_number = models.BigIntegerField(unique=True, db_index=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=200, blank=True)
	is_staff = models.BooleanField(default=False, help_text=('True for admin and false for others'))
	is_active = models.BooleanField(default=True, help_text=('True for active users'))

	objects = CustomUserManager()

	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def get_full_name(self):
		return self.first_name + " " + self.last_name

	def get_short_name(self):
		return self.last_name

	def __unicode__(self):
		return str(self.phone_number)

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from managers import CustomUserManager

"""
Contains custom user model
"""

class User(AbstractBaseUser, PermissionsMixin):
	phone_number = models.BigIntegerField(unique=True, db_index=True)
	first_name = models.CharField(max_length=50, blank=True)
	last_name = models.CharField(max_length=50, blank=True)
	email = models.EmailField(blank=True)
	is_staff = models.BooleanField(defaut=False, help_text=('True for admin and false for others'))
	is_active = models.BooleanField(defaut=True, help_text=('True for active users'))

	objects = CustomUserManager

	USERNAME_FIELD = phone_number
	REQUIRED_FIELDS = []

	def get_full_name(self):
		return self.first_name + " " + self.last_name

	def get_short_name(self):
		return self.last_name
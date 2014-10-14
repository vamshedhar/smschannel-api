from django.contrib.auth.models import BaseUserManager

class CustomUserManage(BaseUserManager):

	def _create_user(self, phone_number, password, is_staff, is_superuser):
		user = self.model(phone_number=phone_number, is_staff=is_staff, is_active=True, is_superuser=is_superuser)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, phone_number, password=None):
		return self._create_user(phone_number, password, False, False)

	def create_superuser(self, phone_number, password):
		return self._create_user(phone_number, password, True, True)
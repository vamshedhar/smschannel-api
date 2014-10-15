from rest_framework import serializers

from users.models import User
from api.models import Group, PhoneBookLog, UserDetail, GroupMessageLog, SingleMessageLog

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('phone_number', 'first_name', 'last_name', 'email',)
		read_only_fields = ()
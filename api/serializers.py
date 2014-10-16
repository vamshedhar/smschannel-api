from rest_framework import serializers

from users.models import User
from api.models import Group, PhoneBookLog, UserPrivileges, GroupMessageLog, SingleMessageLog

class PhoneBookLogSerializer(serializers.ModelSerializer):

	class Meta:
		model = PhoneBookLog
		fields = ('name', 'phone_number', 'member_type', 'groups', 'added_by', 'added_on',)
		read_only_fields = ()

class GroupSerializer(serializers.ModelSerializer):
	members = PhoneBookLogSerializer()
	# members = serializers.Field(source='members')

	class Meta:
		model = Group
		fields = ('name', 'description', 'head', 'members', 'privileged_users',)
		read_only_fields = ()

class UserSerializer(serializers.ModelSerializer):
	head_of = GroupSerializer()

	class Meta:
		model = User
		fields = ('phone_number', 'first_name', 'last_name', 'email', 'head_of', 'privileges',)
		read_only_fields = ('phone_number',)

class GroupMessageLogsSerializer(serializers.ModelSerializer):
	sent_to = GroupSerializer()
	sent_by = UserSerializer()
	# sent_by = serializers.serialize('sent_by', User.objects.all())

	class Meta:
		model = GroupMessageLog
		fields = ('sent_by',  'sent_to', 'message', 'sent_on', 'delivery_status')

class SingleMessageLogsSerializer(serializers.ModelSerializer):
	sent_to = PhoneBookLogSerializer()
	sent_by = UserSerializer()
	
	class Meta:
		model = SingleMessageLog
		fields = ('sent_by',  'sent_to', 'message', 'sent_on', 'delivery_status')
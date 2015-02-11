from rest_framework import serializers

from .models import GroupMessage, SingleMessage

from users.serializers import UserSerializer

from phonebook.serializers import PhoneBookContactSerializer, GroupWithMembersSerializer

class GroupMessageSerializer(serializers.ModelSerializer):
  sent_by = UserSerializer(read_only=True)

  class Meta:
    model = GroupMessage
    fields = ('id', 'sent_to', 'message', 'sent_by', 'sent_on', 'created', 'modified')
    read_only_fields = ('id',)

class SingleMessageSerializer(serializers.ModelSerializer):
  sent_by = UserSerializer(read_only=True)

  class Meta:
    model = SingleMessage
    fields = ('id', 'sent_to', 'message', 'sent_by', 'sent_on', 'created', 'modified')
    read_only_fields = ('id',)

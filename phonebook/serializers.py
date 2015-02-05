from rest_framework import serializers

from .models import Group, PhoneBookContact

from users.serializers import UserSerializer

class PhoneBookContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = PhoneBookContact
    fields = ('id', 'name', 'phone_number', 'type', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ('id', 'name', 'description', 'head', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

class PhoneBookWithGroupsSerializer(serializers.ModelSerializer):
  groups = GroupSerializer(many=True)

  class Meta:
    model = PhoneBookContact
    fields = ('id', 'name', 'phone_number', 'type', 'groups', 'messages', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')
    read_only_fields = ('id', 'messages', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

class GroupWithMembersSerializer(serializers.ModelSerializer):
  members = PhoneBookContactSerializer()

  class Meta:
    model = Group
    fields = ('id', 'name', 'description', 'head', 'members', 'messages', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

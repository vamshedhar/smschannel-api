from rest_framework import serializers

from .models import Group, PhoneBookContact, GroupMember

from base.exceptions import ValidationError

class PhoneBookContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = PhoneBookContact
    fields = ('id', 'name', 'phone_number', 'type', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ('id', 'name', 'description', 'head', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

class PhoneBookWithGroupsSerializer(serializers.ModelSerializer):
  groups = GroupSerializer(many=True, read_only=True)

  class Meta:
    model = PhoneBookContact
    fields = ('id', 'name', 'phone_number', 'type', 'groups', 'messages', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')
    read_only_fields = ('id', 'messages', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

  def validate_phone_number(self, value):
    try:
      PhoneBookContact.objects.get(phone_number=value, deleted_by=None)
      raise ValidationError('Another ACTIVE contact with same number exists')
    except Customer.DoesNotExist:
      pass
    return value

class GroupWithMembersSerializer(serializers.ModelSerializer):
  members = PhoneBookContactSerializer(many=True, read_only=True)

  class Meta:
    model = Group
    fields = ('id', 'name', 'description', 'head', 'members', 'messages', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified', 'authorized_users')
    read_only_fields = ('id', 'messages', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

class GroupMembersSerializer(serializers.ModelSerializer):
  group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.filter(deleted_by=None), required=True)
  member = serializers.PrimaryKeyRelatedField(queryset=PhoneBookContact.objects.filter(deleted_by=None), required=True)

  class Meta:
    model = GroupMember
    fields = ('id', 'group', 'member', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')
    read_only_fields = ('id', 'created_by', 'modified_by', 'deleted_by', 'created', 'modified')

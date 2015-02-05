from rest_framework import serializers

from .models import User

from phonebook.serializers import GroupSerializer

class UserSerializer(serializers.ModelSerializer):
  privileges = GroupSerializer(many=True, read_only=True)
  head_of = GroupSerializer(many=True, read_only=True)

  class Meta:
    model = User
    fields = ('id', 'phone_number', 'first_name', 'last_name', 'email', 'privileges', 'head_of')

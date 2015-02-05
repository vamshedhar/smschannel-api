from rest_framework import serializers

from .models import GroupMessage, SingleMessage

class GroupMessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = GroupMessage
    fields = ('id', 'sent_to', 'message', 'sent_by', 'sent_on', 'delivery_status', 'created', 'modified')
    read_only_fields = ('id',)

class SingleMessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = SingleMessage
    fields = ('id', 'sent_to', 'message', 'sent_by', 'sent_on', 'delivery_status', 'created', 'modified')
    read_only_fields = ('id',)

from rest_framework import serializers

from .models import MessageDetails

class MessageDetailsSerializer(serializers.ModelSerializer):

  class Meta:
    model = MessageDetails
    fields = ('id', 'sent_to', 'type', 'request_id', 'provider', 'number_list', 'message_ids', 'sent', 'status_list', 'response_code')
    read_only_fields = ('id',)

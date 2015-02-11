from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.response import Response

from phonebook.models import PhoneBookContact, Group
from sms.models import MessageDetails
from .models import GroupMessage, SingleMessage

from phonebook.serializers import PhoneBookContactSerializer, GroupWithMembersSerializer
from .serializers import GroupMessageSerializer, SingleMessageSerializer

from base.views import SMSBaseViewset

# Create your views here.

class GroupMessageViewset(SMSBaseViewset):

  queryset = GroupMessage.objects.all()
  serializer_class = GroupMessageSerializer

class SingleMessageViewset(SMSBaseViewset):

  queryset = SingleMessage.objects.all()
  serializer_class = SingleMessageSerializer

  def create(self, request, *args, **kwargs):
    message_data = request.data
    sent_to = message_data.get('sent_to', None)
    message = message_data.get('message', None)

    if not message:
      return Response({
        'SMS': 'Rejected: Empty message cannot be sent.'
      }, status=status.HTTP_400_BAD_REQUEST)

    if not sent_to:
      return Response({
        'SMS': 'Rejected: Message has no sent to.'
      }, status=status.HTTP_400_BAD_REQUEST)

    try:
      contact = PhoneBookContact.objects.get(id=sent_to)
      contact_data = PhoneBookContactSerializer(contact).data
      number_list = contact_data.get('phone_number')
    except PhoneBookContact.DoesNotExist:
      return Response({
        'SMS': 'Rejected: Invalid contact ID.'
      }, status=status.HTTP_400_BAD_REQUEST)

      sms = MessageDetails(type='single', request_id=sent_to)



from django.shortcuts import render

from rest_framework import viewsets, permissions, exceptions, status
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from phonebook.models import PhoneBookContact, Group
from sms.models import MessageDetails
from .models import GroupMessage, SingleMessage

from phonebook.serializers import PhoneBookContactSerializer, GroupWithMembersSerializer
from .serializers import GroupMessageSerializer, SingleMessageSerializer
from sms.serializers import MessageDetailsSerializer

from base.views import SMSBaseViewset

# Create your views here.

class GroupMessageViewset(SMSBaseViewset):

  queryset = GroupMessage.objects.all()
  serializer_class = GroupMessageSerializer

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
      group = Group.objects.get(id=sent_to)
      group_data = GroupWithMembersSerializer(group).data
      number_list = []
      group_members = group_data.get('members')

      for member in group_members:
        phone_number = member.get('phone_number')
        number_list.append(phone_number)

      number_list = ','.join(number_list)
    except Group.DoesNotExist:
      return Response({
        'SMS': 'Rejected: Invalid Group ID.'
      }, status=status.HTTP_400_BAD_REQUEST)

    group_message = GroupMessage(sent_to_id=sent_to, message=message, sent_by=self.request.user)
    group_message.save()

    group_message_data = GroupMessageSerializer(group_message).data

    sms = {
      'number_list': number_list,
      'message': message
    }

    message_details = MessageDetails(type='group', request_id=group_message_data.get('id'), sent_to=sent_to, number_list=number_list, message=message, sent_by=self.request.user)

    message_details.save()
    sms = message_details.send(sms)

    message_details.message_ids = sms.get('message_ids')
    message_details.status_list = sms.get('status_list')
    message_details.response_code = sms.get('response_code')
    message_details.sent = True

    message_details.save()

    return Response(group_message_data, status=status.HTTP_201_CREATED)

  @detail_route(methods=['GET'])
  def delivery_status(self, request, *args, **kwargs):
    obj = self.get_object()
    group_message_data = GroupMessageSerializer(obj).data

    message_details = MessageDetails.objects.get(request_id=group_message_data.get('id')).delivery_status()
    message_details_data = MessageDetailsSerializer(message_details).data
    group_message_data.update({
        'message_details': message_details_data
      })
    return Response(group_message_data, status=status.HTTP_201_CREATED)

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

    single_message = SingleMessage(sent_to_id=sent_to, message=message, sent_by=self.request.user)
    single_message.save()

    single_message_data = SingleMessageSerializer(single_message).data

    sms = {
      'number_list': number_list,
      'message': message
    }

    message_details = MessageDetails(type='single', request_id=single_message_data.get('id'), sent_to=sent_to, number_list=number_list, message=message, sent_by=self.request.user)

    message_details.save()
    sms = message_details.send(sms)

    message_details.message_ids = sms.get('message_ids')
    message_details.status_list = sms.get('status_list')
    message_details.response_code = sms.get('response_code')
    message_details.sent = True

    message_details.save()

    return Response(single_message_data, status=status.HTTP_201_CREATED)

  @detail_route(methods=['GET'])
  def delivery_status(self, request, *args, **kwargs):
    obj = self.get_object()
    single_message_data = SingleMessageSerializer(obj).data

    message_details = MessageDetails.objects.get(request_id=single_message_data.get('id')).delivery_status()
    message_details_data = MessageDetailsSerializer(message_details).data
    single_message_data.update({
        'message_details': message_details_data
      })
    return Response(single_message_data, status=status.HTTP_201_CREATED)



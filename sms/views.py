from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import MessageDetails
from smslogs.models import GroupMessage, SingleMessage

# Create your views here.

@api_view(('POST',))
def send_sms(request, format=None):
  '''
  Sends SMS on POST call
  '''

  data = request.data
  request_id = data.get('request_id', None)
  request_type = data.get('request_type', None)
  number_list = data.get('number_list', None)

  if not request_id:
    return Response({
      'SMS': 'Rejected: Group/Contact ID not specified(request_id).'
    }, status=status.HTTP_400_BAD_REQUEST)

  if request_type == 'single':
    try:
      single_message = SingleMessage.objects.get(id=request_id, deleted_by=None)
    except SingleMessage.DoesNotExist:
      return Response({
        'SMS': 'Rejected: Invalid contact ID.'
      }, status=status.HTTP_400_BAD_REQUEST)

  if request_type == 'group':
    try:
      single_message = GroupMessage.objects.get(id=request_id, deleted_by=None)
    except GroupMessage.DoesNotExist:
      return Response({
        'SMS': 'Rejected: Invalid group ID.'
      }, status=status.HTTP_400_BAD_REQUEST)

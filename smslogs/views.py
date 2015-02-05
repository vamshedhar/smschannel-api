from django.shortcuts import render

from rest_framework import viewsets, permissions

from .models import GroupMessage, SingleMessage
from .serializers import GroupMessageSerializer, SingleMessageSerializer

from base.views import SMSBaseViewset

# Create your views here.

class GroupMessageViewset(SMSBaseViewset):

  queryset = GroupMessage.objects.all()
  serializer_class = GroupMessageSerializer

class SingleMessageViewset(SMSBaseViewset):

  queryset = SingleMessage.objects.all()
  serializer_class = SingleMessageSerializer

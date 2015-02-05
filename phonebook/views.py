from django.shortcuts import render

from rest_framework import viewsets, permissions

from .models import Group, PhoneBookContact
from .serializers import GroupWithMembersSerializer, PhoneBookWithGroupsSerializer

from base.views import PhoneBookBaseViewset

# Create your views here.

class GroupViewSet(PhoneBookBaseViewset):

  queryset = Group.objects.all()
  serializer_class = GroupWithMembersSerializer

class PhoneBookViewSet(PhoneBookBaseViewset):

  queryset = PhoneBookContact.objects.all()
  serializer_class = PhoneBookWithGroupsSerializer

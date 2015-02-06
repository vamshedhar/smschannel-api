from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy

from .models import Group, PhoneBookContact
from .serializers import GroupWithMembersSerializer, PhoneBookWithGroupsSerializer

from base.views import PhoneBookBaseViewset

# Create your views here.

class APIRootView(APIView):
  """
  API Root:

  List of API end point of the project.

  Each list has a details view by passing ID at the end of the url.
  """
  def get(self, request):
    data = {
      'admin': reverse('admin:index', request=request),
      'api_root': reverse('api_root', request=request),
      'phonebook': reverse('api:phonebook-list', request=request),
      'groups': reverse('api:groups-list', request=request),
      'single-message': reverse('api:single-message-list', request=request),
      'group-message': reverse('api:group-message-list', request=request),
      'users': reverse('api:users-list', request=request),
    }
    return Response(data)

class GroupViewset(PhoneBookBaseViewset):

  queryset = Group.objects.all()
  serializer_class = GroupWithMembersSerializer

class PhoneBookViewset(PhoneBookBaseViewset):

  queryset = PhoneBookContact.objects.all()
  serializer_class = PhoneBookWithGroupsSerializer

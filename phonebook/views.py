from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Group, PhoneBookContact, GroupMember
from .serializers import GroupWithMembersSerializer, PhoneBookWithGroupsSerializer, GroupMembersSerializer

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
      'api-root': reverse('api_root', request=request),
      'phonebook': reverse('api:phonebook-list', request=request),
      'faculty': reverse('api:phonebook-faculty', request=request),
      'students': reverse('api:phonebook-students', request=request),
      'staff': reverse('api:phonebook-staff', request=request),
      'groups': reverse('api:groups-list', request=request),
      'group-members': reverse('api:group-members-list', request=request),
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

  @list_route(methods=['GET'])
  def staff(self, request, *args, **kwargs):
    self.queryset = self.queryset.filter(type="Staff")
    return super(PhoneBookViewset, self).list(request,*args,**kwargs)

  @list_route(methods=['GET'])
  def faculty(self, request, *args, **kwargs):
    self.queryset = self.queryset.filter(type="Faculty")
    return super(PhoneBookViewset, self).list(request,*args,**kwargs)

  @list_route(methods=['GET'])
  def students(self, request, *args, **kwargs):
    self.queryset = self.queryset.filter(type="Student")
    return super(PhoneBookViewset, self).list(request,*args,**kwargs)

class GroupMembersViewset(PhoneBookBaseViewset):

  queryset = GroupMember.objects.all()
  serializer_class = GroupMembersSerializer

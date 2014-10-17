from django.shortcuts import render
from rest_framework import generics, permissions

from users.models import User
from api.models import Group, PhoneBookLog, UserPrivileges, GroupMessageLog, SingleMessageLog

from api.serializers import UserSerializer, GroupSerializer, PhoneBookLogSerializer, GroupMessageLogsSerializer, SingleMessageLogsSerializer

# Create your views here.

class PhoneBookLogsView(generics.ListCreateAPIView):
	'''
	Endpoint to get phone book entries and add new entry
	'''

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	model = PhoneBookLog
	serializer_class = PhoneBookLogSerializer


class GroupListView(generics.ListCreateAPIView):
	'''
	Endpoint to get group list and add new group
	'''

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	model = Group
	serializer_class = GroupSerializer


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
	'''
	Endpoint to get and update profile of a `User`.
	'''

	permission_classes = (permissions.IsAuthenticated,)

	model = User
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user

class GroupMessageLogsView(generics.ListCreateAPIView):
	'''
	Endpoint to get group Msessage Logs
	'''

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	model = GroupMessageLog
	serializer_class = GroupMessageLogsSerializer	

class SingleMessageLogsView(generics.ListCreateAPIView):
	'''
	Endpoint to get Single Msessage Logs
	'''

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	model = SingleMessageLog
	serializer_class = SingleMessageLogsSerializer
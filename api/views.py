from django.shortcuts import render
from rest_framework import generics

from users.models import User
from api.models import Group, PhoneBookLog, UserPrivileges, GroupMessageLog, SingleMessageLog

from api.serializers import UserSerializer, GroupSerializer, PhoneBookLogSerializer, GroupMessageLogsSerializer, SingleMessageLogsSerializer

# Create your views here.

class PhoneBookLogsView(generics.ListCreateAPIView):
	'''
	Endpoint to get phone book entries and add new entry
	'''

	model = PhoneBookLog
	serializer_class = PhoneBookLogSerializer


class GroupListView(generics.ListCreateAPIView):
	'''
	Endpoint to get group list and add new group
	'''

	model = Group
	serializer_class = GroupSerializer


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
	'''
	Endpoint to get and update profile of a `User`.
	'''

	model = User
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user

class GroupMessageLogsView(generics.ListCreateAPIView):
	'''
	Endpoint to get group Msessage Logs
	'''

	model = GroupMessageLog
	serializer_class = GroupMessageLogsSerializer	

class SingleMessageLogsView(generics.ListCreateAPIView):
	'''
	Endpoint to get Single Msessage Logs
	'''

	model = SingleMessageLog
	serializer_class = SingleMessageLogsSerializer
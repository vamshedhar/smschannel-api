from django.shortcuts import render
from rest_framework import generics

from users.models import User
from api.models import Group, PhoneBookLog, UserDetail, GroupMessageLog, SingleMessageLog

from api.serializers import UserSerializer

# from rest_framework.views import APIView
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# @api_view(['GET'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))

class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
	'''
	Endpoint to get and update profile of a `User`.
	'''
	# authentication_classes = (SessionAuthentication, BasicAuthentication)
	# permission_classes = (IsAuthenticated,)

	model = User
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user
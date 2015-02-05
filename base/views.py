from django.shortcuts import render

from rest_framework import viewsets, permissions

# Create your views here.

class SMSBaseViewset(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticated,)
  lookup_field = 'id'

  def pre_save(self, message):
    message.sent_by = self.request.user

class PhoneBookBaseViewset(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticated,)
  lookup_field = 'id'

  def pre_save(self, message):
    message.created_by = self.request.user

  def pre_delete(self, message):
    message.deleted_by = self.request.user


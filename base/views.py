from django.shortcuts import render

from rest_framework import viewsets, permissions

# Create your views here.

class SMSBaseViewset(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticated,)
  lookup_field = 'id'

  def pre_save(self, message):
    message.sent_by = self.request.user

from django.shortcuts import render

from rest_framework import viewsets, permissions

from base.filters import DeletedObjectsFilter, UserMessagesFilter

# Create your views here.

class SMSBaseViewset(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticated,)
  lookup_field = 'id'
  filter_backends = (UserMessagesFilter,)

  def perform_create(self, serializer):
    serializer.save(sent_by=self.request.user)

class PhoneBookBaseViewset(viewsets.ModelViewSet):
  permission_classes = (permissions.IsAuthenticated,)
  filter_backends = (DeletedObjectsFilter,)
  lookup_field = 'id'

  def perform_update(self, serializer):
    serializer.save(modified_by=self.request.user)

  def perform_create(self, serializer):
    serializer.save(created_by=self.request.user)

  def perform_destroy(self, instance):
    instance.deleted_by = self.request.user
    instance.delete()

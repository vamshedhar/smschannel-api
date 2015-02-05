from rest_framework import filters

class UserMessagesFilter(filters.BaseFilterBackend):

  # Filter allows user to see only the messages that he sent.

  def filter_queryset(self, request, queryset, view):
    return queryset.filter(sent_by=request.user)

class DeletedObjectsFilter(filters.BaseFilterBackend):

  # Filter that only allows users to see objects that were not deleted

  def filter_queryset(self, request, queryset, view):
    return queryset.filter(deleted_by=None)

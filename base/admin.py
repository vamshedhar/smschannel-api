from django.contrib import admin

# Register your models here.

class PhoneBookBaseAdmin(admin.ModelAdmin):

  class Meta:
    abstract = True

  def get_queryset(self, request):

    # Override queryset to show only objects which are not deleted.
    query = super(PhoneBookBaseAdmin, self).get_queryset(request)
    if request.user.is_superuser:
      return query
    return query.filter(deleted_by=None)

  def save_model(self, request, obj, form, change):

    # When creating a new object, set the created_by field.
    if not change:
      obj.created_by = request.user
    obj.save()

  def delete_model(self, request, obj, form, change):

    # When deleting an object, set the deleted_by field.
    if not change:
      obj.deleted_by = request.user
    obj.delete()

class SMSBaseAdmin(admin.ModelAdmin):

  readonly_fields = ('sent_to', 'message',)

  class Meta:
    abstract = True

  def get_queryset(self, request):

    # Override queryset to show only messages which are sent by user.
    query = super(SMSBaseAdmin, self).get_queryset(request)
    if request.user.is_superuser:
      return query
    return query.filter(sent_by=request.user)

  def save_model(self, request, obj, form, change):

    # When sending a new message, set the sent_by field.
    if not change:
      obj.sent_by = request.user
    obj.save()

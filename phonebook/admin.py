from django.contrib import admin

from .models import Group, PhoneBookContact

# Register your models here.

models_to_register = [
    Group, PhoneBookContact
]

class GroupAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'description', 'created_by')

  def save_model(self, request, obj, form, change):
    """When creating a new object, set the creator field.
    """
    if not change:
        obj.created_by = request.user
    obj.save()

class PhoneBookContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'phone_number', 'created_by')

  def save_model(self, request, obj, form, change):
    """When creating a new object, set the creator field.
    """
    if not change:
        obj.created_by = request.user
    obj.save()

def register_models(models):
  for model in models:
    admin.site.register(model)

# register_models(models_to_register)

admin.site.register(Group, GroupAdmin)
admin.site.register(PhoneBookContact, PhoneBookContactAdmin)

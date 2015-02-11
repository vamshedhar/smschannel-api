from django.contrib import admin

from .models import MessageDetails

from base.admin import SMSBaseAdmin

# Register your models here.

class MessageDetailsAdmin(SMSBaseAdmin):
  list_display = ('id', 'type', 'number_list', 'message', 'provider', 'message_ids', 'sent', 'status_list', 'response_code', 'sent_on')

admin.site.register(MessageDetails, MessageDetailsAdmin)

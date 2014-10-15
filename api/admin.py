from django.contrib import admin

from api.models import Group, PhoneBookLog, UserDetail, GroupMessageLog, SingleMessageLog
# Register your models here.

admin.site.register(PhoneBookLog)
admin.site.register(Group)
admin.site.register(UserDetail)
admin.site.register(GroupMessageLog)
admin.site.register(SingleMessageLog)
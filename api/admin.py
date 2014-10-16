from django.contrib import admin

from api.models import Group, PhoneBookLog, UserPrivileges, GroupMessageLog, SingleMessageLog
# Register your models here.

admin.site.register(PhoneBookLog)
admin.site.register(Group)
admin.site.register(UserPrivileges)
admin.site.register(GroupMessageLog)
admin.site.register(SingleMessageLog)
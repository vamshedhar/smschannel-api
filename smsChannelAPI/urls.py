from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

from rest_framework import routers

from phonebook import views as PhoneBookViews
from smslogs.views import GroupMessageViewset, SingleMessageViewset
from phonebook.views import GroupViewset, PhoneBookViewset, GroupMembersViewset, APIRootView, FacultyViewset, StaffViewset, StudentViewset
from users.views import UserViewset

router = routers.SimpleRouter()
router.register(r'phonebook', PhoneBookViewset, base_name="phonebook")
router.register(r'faculty', FacultyViewset, base_name="faculty")
router.register(r'staff', StaffViewset, base_name="staff")
router.register(r'students', StudentViewset, base_name="student")
router.register(r'groups', GroupViewset, base_name="groups")
router.register(r'group-members', GroupMembersViewset, base_name="group-members")
router.register(r'single-message', SingleMessageViewset, base_name="single-message")
router.register(r'group-message', GroupMessageViewset, base_name="group-message")
router.register(r'users', UserViewset, base_name="users")

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='api/login/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace="rest_framework")),
    url(r'^api/', include(router.urls, namespace="api")),
    url(r'^api-root/', APIRootView.as_view(), name="api_root"),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/api-root/')),
    url(r'^auth-token/', 'rest_framework_jwt.views.obtain_jwt_token', name="auth"),
)

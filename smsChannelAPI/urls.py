from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from smslogs.views import GroupMessageViewset, SingleMessageViewset
from phonebook.views import GroupViewSet, PhoneBookViewSet
from users.views import UserViewset

router = routers.SimpleRouter()
router.register(r'phonebook', PhoneBookViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'single-message', SingleMessageViewset)
router.register(r'group-message', GroupMessageViewset)
router.register(r'users', UserViewset)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smsChannelAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth-token/', 'rest_framework_jwt.views.obtain_jwt_token'),
)

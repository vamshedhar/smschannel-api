from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

from rest_framework import routers

from smslogs.views import GroupMessageViewset, SingleMessageViewset
from phonebook.views import GroupViewset, PhoneBookViewset
from users.views import UserViewset

router = routers.SimpleRouter()
router.register(r'phonebook', PhoneBookViewset)
router.register(r'groups', GroupViewset)
router.register(r'single-message', SingleMessageViewset)
router.register(r'group-message', GroupMessageViewset)
router.register(r'users', UserViewset)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smsChannelAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', RedirectView.as_view(url='api/login/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/api/phonebook/')),
    url(r'^auth-token/', 'rest_framework_jwt.views.obtain_jwt_token'),
)

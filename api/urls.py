from django.conf.urls import url, patterns, include
from api.views import UserRetrieveUpdateView

urlpatterns = patterns('api.views',
    # Examples:
    # url(r'^$', 'smsChannelAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^', include('api.urls')),
    # url(r'^auth-token/', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^users/$', UserRetrieveUpdateView.as_view()),
)
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from .views import PostRudView, PostAPIView
# from django.

app_name = 'api-post'

urlpatterns = [
    re_path(r'auth/login/?', obtain_auth_token, name='api-login'),
    re_path(r'^$', PostAPIView.as_view(), name='post-listcreate'),
    re_path(r'^(?P<pk>\d+)/$', PostRudView.as_view(), name='post-rud'),
]

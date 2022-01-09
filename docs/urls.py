from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    docs_view,
    docs_usage_installation_view,
    token_api_view,
    DevAPIView
)

urlpatterns = [
    path('', docs_view, name="docs"),
    path('installation&usage/', docs_usage_installation_view, name="docs_install_usage"),
    path('auth-api/user/keys/46/', token_api_view, name='api-key'),
    path('auth-api/user/key/46/', DevAPIView.as_view(), name='api-show'),
]

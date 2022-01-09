from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

from users.views import (
    home_view,
    login_view,
    logout_view,
    register_view,
    admin_view,
)

urlpatterns = [
    path('', home_view, name="home"),
    re_path(r'docs?/', include('docs.urls'), name="docs"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('admin121234admin2345678admin2345678/', admin.site.urls, name="whoami"),
    path('admin/', admin_view, name="admin"),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/', include('core.api.urls'), name='core'),
] 

urlpatterns += static(settings.STATIC_URL, 
                document_root=settings.STATIC_ROOT)

from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from MyApp import views
from rest_framework_jwt.views import refresh_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^idealweight/',views.IdealWeight),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),
]




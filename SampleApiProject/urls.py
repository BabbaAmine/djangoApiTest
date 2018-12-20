from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from MyApp import views
from rest_framework_jwt.views import refresh_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^addMsgToRoom/$', views.addMsgToRoom),
    url(r'^getRoomMsgs/(?P<idroom>[0-9]+)$', views.getRoomMsgs),
    url(r'^getLastRoomMsg/(?P<idroom>[0-9]+)$', views.getLastRoomMsg),
    url(r'^addRoom/$', views.addRoom),
    url(r'^getUserRooms/(?P<iduser>[0-9]+)$', views.getUserRooms),
    url(r'^addFreind/$', views.addFreind),
    url(r'^accept_ignore_Freind/(?P<iduser>[0-9]+)$', views.accept_ignore_Freind),
    url(r'^getUsersByEmail_Nom_Prenom/(?P<text>[\w\-]+)$', views.getUsersByEmail_Nom_Prenom),
    url(r'^getUsersByEmail_F/(?P<iduser>[0-9]+)$', views.getUserFreinds),
]




from django.urls import path

from .views import *


urlpatterns = [
    path('getusers/', UserView.as_view()),
    path('editstaff/<int:pk>/', EditUserView.as_view()),

    path('getclients/', ClientView.as_view()),
    path('getclients/<int:pk>/', EditClientView.as_view()),

    path('getgroups/', GroupsView.as_view()),
    path('testlogin/', testLogin.as_view()),

    path('stafflogin/', StaffLogin.as_view()),

    path('clientlogin/', ClientLogin.as_view()),
    path('clientinfo/', ClientInfo.as_view()),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),

]

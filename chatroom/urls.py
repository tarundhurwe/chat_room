from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('<str:room>/', views.room, name = "room"),
    path('check', views.check, name = "check"),
    path('send', views.send, name = "send"),
    path('getmessages/<str:room>/', views.fetch_messages, name = "fetchmessages")
]
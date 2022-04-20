from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('terms_of_service', views.terms_of_service, name="terms_of_service"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('monitor', views.monitor, name="monitor"),
    path('autologin/<str:system>', views.autologin, name="autologin"),
]

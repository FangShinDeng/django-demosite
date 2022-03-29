"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('', include('account.urls')),
    path('captcha/', include('captcha.urls')),
    # accounts/ signup/ [name='account_signup']
    # accounts/ login/ [name='account_login']
    # accounts/ logout/ [name='account_logout']
    # accounts/ password/change/ [name='account_change_password']
    # accounts/ password/set/ [name='account_set_password']
    # accounts/ inactive/ [name='account_inactive']
    # accounts/ email/ [name='account_email']
    # accounts/ confirm-email/ [name='account_email_verification_sent']
    # accounts/ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
    # accounts/ password/reset/ [name='account_reset_password']
    # accounts/ password/reset/done/ [name='account_reset_password_done']
    # accounts/ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
    # accounts/ password/reset/key/done/ [name='account_reset_password_from_key_done']
]

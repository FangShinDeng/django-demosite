from tkinter import Widget
from django.db import models
from django import forms 
from django.contrib.auth.models import User, Group
# from allauth.account.models import 
from allauth.app_settings import USER_MODEL
from django.contrib.sessions.models import Session
from django.utils.translation import gettext_lazy as _
# allauth.account.signals.user_logged_in

# Create your models here.
class LoggedInUser(models.Model):
    user = models.OneToOneField(USER_MODEL, related_name='logged_in_user', on_delete=models.SET_NULL, null=True)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True)
    online = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username

    def __repr__(self) -> str:
        return self.user.username

    def get_session_data(self):
        if self.session:
            return self.session.get_decoded()
        else:
            return None

    def get_session_expire(self):
        if self.session:
            return self.session.expire_date
        else:
            return None

    class Meta:
        default_permissions = ("view", "delete")


# class LoginSystemMode(models.Model):
#     name = models.CharField(max_length=64) # method name, lik

class LoginSystem(models.Model):
    # mode = models.ForeignKey(LoginSystemMode, on_delete=models.CASCADE)
    name = models.CharField(max_length=64) # portal, hrmis
    url = models.URLField()
    form_elements_name = models.TextField(blank=True, null=True) # "" means no soup
    login_element = models.CharField(max_length=32)
    password_element = models.CharField(max_length=32)
    extra_headers = models.TextField(blank=True, null=True)
    redirect_url = models.URLField() # first redirect page
    # groups = models.ManyToManyField(Group, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class LoginSystemStatus(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.SET_NULL, null=True)
    system = models.OneToOneField(LoginSystem, on_delete=models.CASCADE)
    account = models.CharField(max_length=64)
    password = models.CharField(_('password'), max_length=128)
    cookies = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)    
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    last_logout = models.DateTimeField(_('last logout'), blank=True, null=True)
    # keys = 

    def __str__(self):
        return self.user.username

    def __repr__(self):
        return self.user.username
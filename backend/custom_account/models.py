from django.db import models
from django.contrib.auth.models import User
# from allauth.account.models import 
from allauth.app_settings import USER_MODEL
from django.contrib.sessions.models import Session
# allauth.account.signals.user_logged_in

# Create your models here.
class LoggedInUser(models.Model):
    user = models.OneToOneField(USER_MODEL, related_name='logged_in_user', on_delete=models.SET_NULL, null=True)
    # session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True)
    online = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username

    def __repr__(self) -> str:
        return self.user.username

    def get_session_data(self):
        return self.session

from ipaddress import ip_address
from django.db.models.signals import post_save
from .models import LoggedInUser, User
from django.dispatch import receiver
from allauth.account.signals import user_logged_in, user_logged_out
from .modules import get_ip
from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# post_save.connect(create_profile, sender=User)

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    ip_address = get_ip(request)
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))
    LoggedInUser.objects.filter(user=kwargs.get('user')).update(online=True, ip_address=ip_address, session=request.session.session_key) # , session_key=request.session.session_key
    message = f"user login: {request.user}, ip_address: {ip_address}"
    LogEntry.objects.log_action(
        user_id=request.user.id,
        content_type_id=ContentType.objects.get_for_model(LoggedInUser, for_concrete_model=True).id,
        action_flag=ADDITION,
        object_id=LoggedInUser.objects.get(user_id=request.user.id).id,
        object_repr=message,
        change_message=message
    )
    

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    ip_address = get_ip(request)
    message = f"logout: {request.user}, ip_address: {ip_address}"
    LogEntry.objects.log_action(
        user_id=request.user.id,
        content_type_id=ContentType.objects.get_for_model(LoggedInUser, for_concrete_model=True).id,
        action_flag=DELETION,
        object_id=LoggedInUser.objects.get(user_id=request.user.id).id,
        object_repr=message,
        change_message=message
    )
    LoggedInUser.objects.filter(user=kwargs.get('user')).update(online=False, ip_address=ip_address) # LoggedInUser.objects.filter(user=kwargs.get('user')).delete() request.session.session_key

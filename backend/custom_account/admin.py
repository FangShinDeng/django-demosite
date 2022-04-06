from django.contrib import admin
from . import models 
from django.http import HttpRequest
from django.contrib.admin.models import LogEntry

# Register your models here.
def getModelFields(model):
    return [field.name for field in model._meta.get_fields()]

class DjangoAdminLog_Admin(admin.ModelAdmin):

    list_display = ['id', 'action_time', 'user', 'action_flag','content_type', '__str__', 'object_id', 'object_repr']
    list_display_links = ['action_time']
    list_filter = ['action_time', 'content_type', 'user']
    list_per_page = 50
    readonly_fields = ['action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message']

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser

class LoggedInUser_Admin(admin.ModelAdmin): # list_display = ['id', 'user_id', 'session_key']
    list_display = getModelFields(models.LoggedInUser)
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser

from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

admin.site.register(Session, SessionAdmin)
admin.site.register(LogEntry, DjangoAdminLog_Admin)
admin.site.register(models.LoggedInUser, LoggedInUser_Admin)
admin.site.site_header = "Site Header"
admin.site.site_title = "Site Title"
admin.site.index_title = "Index Title"
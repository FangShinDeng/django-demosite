from django.contrib import admin
from . import models 
from django.http import HttpRequest
from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session

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

    list_display = getModelFields(models.LoggedInUser) + ["get_session_data", "get_session_expire"]
    actions = ["kick_user"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    # def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
    #     return False
    # def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
    #     return request.user.is_superuser
    
    # @admin.action(description="kick user", permissions=['delete'])
    # def kick_user(modeladmin, request, queryset):
    #     session_key_list = queryset.values_list('session', flat=True)
    #     sessions = Session.objects.filter(session_key__in=session_key_list)
    #     if sessions:
    #         sessions.delete()
    #     queryset.delete()

    def delete_model(self, request: HttpRequest, obj) -> None:
        if obj.session_id:
            Session.objects.filter(session_key=obj.session_id).delete()
        return super().delete_model(request, obj)
    
    def delete_queryset(self, request: HttpRequest, queryset) -> None:
        session_key_list = queryset.values_list('session', flat=True)
        sessions = Session.objects.filter(session_key__in=session_key_list)
        if sessions:
            sessions.delete()
        return super().delete_queryset(request, queryset)


# class SessionAdmin(admin.ModelAdmin):
#     def _session_data(self, obj):
#         return obj.get_decoded()
#     list_display = ['session_key', '_session_data', 'expire_date']

# admin.site.register(Session, SessionAdmin)
admin.site.register(LogEntry, DjangoAdminLog_Admin)
admin.site.register(models.LoggedInUser, LoggedInUser_Admin)
admin.site.site_header = "Site Header"
admin.site.site_title = "Site Title"
admin.site.index_title = "Index Title"
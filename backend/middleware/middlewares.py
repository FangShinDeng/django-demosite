import threading
import logging
import socket
try:
    from django.utils.deprecation import MiddlewareMixin
except:
    MiddlewareMixin = object

local = threading.local()

class RequestLogFilter(logging.Filter):
    def filter(self, record):
        record.hostname = getattr(local, 'hostname', None)
        record.dest_ip = getattr(local, 'dest_ip', None)
        record.username = getattr(local, 'username', None)
        record.source_ip = getattr(local, 'source_ip', None)
        return True

class RequestLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        local.hostname = socket.gethostname()
        local.dest_ip = socket.gethostbyname(local.hostname) # local.username = request.username
        http_client_ip = request.META.get("HTTP_CLIENT_IP", "")
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
        
        if http_client_ip:
            source_ip = http_client_ip
        elif x_forwarded_for:
            source_ip = x_forwarded_for.split(',')[0]
        else:
            source_ip = request.META.get('REMOTE_ADDR')
        local.source_ip = source_ip

    def process_response(self, request, response):
        return response

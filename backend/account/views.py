from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from allauth.account.views import LoginView
from . import modules
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError

# Create your views here.

@verified_email_required(login_url="account_login")
def home(request):
    # print(request.user.userprofile.email_confirmed)
    context = {}
    return render(request, "dashboard/index.html", context)

def user_profile(request):
    context = {}
    return render(request, "dashboard/user_profile.html", context)

def terms_of_service(request):
    return render(request, "account/terms-of-service.html")

def monitor(request):
    show_list = ["Server IP","REMOTE_ADDR", "HTTP_USER_AGENT"]
    client_ip = modules.get_ip(request)
    # print(f"proxy_ip:{proxy_ip}, client_ip:{client_ip}")
    g = GeoIP2()    
    a = client_ip
    try:
        a = g.city(client_ip)
    except AddressNotFoundError:
        pass 

    context = {
        "meta": request.META, 
        "show_list": show_list,
        "a": a,
        # "b": b,
    }
    return render(request, "monitor.html", context)

# class CustomLoginView(LoginView):
    
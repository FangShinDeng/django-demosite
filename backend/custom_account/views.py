from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from allauth.account.views import LoginView
from . import modules, models
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError
from django.http import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from captcha.models import CaptchaStore
from bs4 import BeautifulSoup
import requests
import time 
import json
from datetime import datetime
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
        a = g.city("")
    except AddressNotFoundError:
        pass 

    context = {
        "meta": request.META, 
        "show_list": show_list,
        "a": a,
        # "b": b,
    }
    return render(request, "monitor.html", context)

@verified_email_required(login_url="account_login")
def autologin(request, system):
    system_info = models.LoginSystem.objects.filter(name=system).values().first()
    system_user = models.LoginSystemStatus.objects.filter(user=request.user.id, system=system_info["id"])
    user_info = system_user.values().first()
    if not system_info or not user_info: return HttpResponseNotFound(content={"message":"didn't found system or user account"})
    payload = {
        system_info["login_element"]: user_info["account"],
        system_info["password_element"]: user_info["password"],
    }
    with requests.Session() as s:
        get_response = s.get(system_info['url'])
        time.sleep(1)
        soup = BeautifulSoup(get_response.text, 'html.parser')
        if system_info["form_elements_name"]:
            other_elements = system_info["form_elements_name"].replace(" ","").split(",")
            for name in other_elements:
                payload[name] = soup.find('input', {'name': name}).get('value')
        cookies = s.cookies.get_dict()
        cookieStr = ""
        for key in cookies:
            cookieStr += f"{key}={cookies[key]}; "
        cookieStr = cookieStr[:-2]
        headers = dict(Cookie=cookieStr)
        post_response = s.post(system_info["url"], data=payload, headers=headers)
        post_cookies = json.dumps(s.cookies.get_dict())
        # print(post_cookies)
        system_user.update(cookies=post_cookies, status=True, last_login=datetime.now())
        # with open(system_info["name"] + '.html', 'w+', encoding='utf-8') as f:
        #     f.write(post_response.text)
        
    return JsonResponse(data=system_info)


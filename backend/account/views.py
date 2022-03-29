from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
# Create your views here.

@verified_email_required(login_url="account_login")
def home(request):
    # print(request.user.userprofile.email_confirmed)
    context = {}
    return render(request, "dashboard/index.html", context)

def user_profile(request):
    context = {}
    return render(request, 'dashboard/user_profile.html', context)

def terms_of_service(request):
    return render(request, 'account/terms-of-service.html')
import sys
from uuid import uuid4
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from accounts.models import Token


def send_login_email(request):
    email = request.POST['email']
    uid = str(uuid4())
    Token.objects.create(email=email, uid=uid)
    print("saving uid", uid, "for_email", email, file=sys.stderr)
    url = request.build_absolute_uri(f'/accounts/login?uid={uid}')
    send_mail(
        'Your login link for Superlists',
        f'Use this link to log in:\n\n{url}',
        'work.it@o2.pl',
        [email],
    )
    
    return render(request, "login_email_sent.html")

def login(request):
    print('login view', file=sys.stderr)
    uid = request.GET.get('uid')
    user = authenticate(uid=uid)
    if user is not None:
        auth_login(request, user)
    return redirect('/')

def logout(request):
    auth_logout(request)
    return redirect('/')
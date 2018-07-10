from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout # 用户登录登出验证
from django.core.cache import cache #缓存
from django.urls import reverse
from .forms import LoginForm, RegForm
from django.http import JsonResponse


def login_for_medal(request):
    login_form = LoginForm(request.POST)
    data = {}
    if login_form.is_valid():
        user = login_form.cleaned_data['user']
        login(request, user)
        data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request,user)
            return redirect(request.GET.get('from'),reverse('home'))
    else:
        login_form = LoginForm()
        return render(request,'user/login.html',{'login_form':login_form})

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            # 登录用户
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()
    return render(request, 'user/register.html', {'reg_form':reg_form})

def user_logout(request):
    # from django.contrib.auth import authenticate,login,logout # 用户登录登出验证
    logout(request)
    return redirect(request.GET.get('from'),reverse('home'))

def user_info(request):
    '''个人资料'''
    ip = request.META['REMOTE_ADDR']
    return render(request,'user/user_info.html',{'ip':ip})

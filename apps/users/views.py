from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.hashers import make_password

from users.forms import LoginForm, RegisterForm
from users.models import UserInfo, EmailVerify
from utils.email_send import send_register_email


# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserInfo.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 首页
class IndexView(View):
    def get(self, request):
        return render(request, 'index.htm', {})


# 登录页面
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)  # 获取到登录的数据
        if login_form.is_valid():  # 验证是不是合法
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)  # 验证user
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {'msg': '用户未激活'})
            else:
                return render(request, "login.html", {'msg': '账号密码有误'})

        return render(request, "login.html", {'login_form': login_form})


# 退出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.htm', {})


# 注册
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        # 获取前段的数据
        register_form = RegisterForm(request.POST)
        # 验证表单是不是合法
        if register_form.is_valid():
            email = request.POST.get("email", "")
            if UserInfo.objects.filter(email=email):
                return render(request, "register.html", {
                    "register_form": register_form,
                    "msg": "用户已经存在!"})

            pass_word = request.POST.get("password", "")

            #  实例化UserProfile字段
            user_profile = UserInfo()
            user_profile.username = email
            user_profile.email = email
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)

            user_profile.save()

            # 发送邮箱
            send_register_email(email, 'register')

            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request, "register.html", {"register_form": register_form})


# 激活
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerify.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserInfo.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, 'success_activate.html')
            return render(request, 'login.html')

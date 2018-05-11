from django import forms

from captcha.fields import CaptchaField
from users.models import UserInfo


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 修改密码的验证字段
class ModifyPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)


# 在自我中心种修改密码的验证字段
class ChangePwdForm(forms.Form):
    email = forms.EmailField(required=True)
    passwordold = forms.CharField(required=True, min_length=6)
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)


# 上传图片
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserInfo  # 说明要引用的model是那个
        fields = ['image']  # 说明要使用的字段有那个


# 用户信息修改
class UploadInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['nick_name', 'gender', 'email', 'phone', 'qq', 'summary','birthday']

# 请求升级
class UpdateUseForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})

# 确认升级
class UpdateSureForm(forms.Form):
    email = forms.EmailField(required=True)


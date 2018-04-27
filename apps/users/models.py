from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.


class UserInfo(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default='female')
    image = models.ImageField(upload_to='image/%Y/%m', default=u"", max_length=100)
    phone = models.CharField(max_length=11, verbose_name=u"手机号码")
    qq = models.IntegerField(null=True, blank=True)
    summary = models.CharField(max_length=400, verbose_name=u"用户简介", null=True, blank=True)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Banner(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"轮播图名")
    image = models.ImageField(upload_to='banner/%Y/%m', default=u"", max_length=100)
    url = models.URLField(max_length=100, verbose_name=u"访问地址")
    index = models.IntegerField(default=0, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class EmailVerify(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=25, verbose_name=u"邮箱")
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('reset', '找回密码')), verbose_name=u"类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)

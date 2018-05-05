from django.conf.urls import url
from users.views import UserInfoView, ChangePwdView, UserOrderView, UserWorkView, UserCourseView, UploadImageView

urlpatterns = [
    # 用户信息
    url(r'info/$', UserInfoView.as_view(), name='info'),

    # 修改密码
    url(r'change_pwd/$', ChangePwdView.as_view(), name='change_pwd'),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    # 我的订单
    url(r'order/$', UserOrderView.as_view(), name="order"),

    # 我的作业
    url(r'homework/$', UserWorkView.as_view(), name="homework"),

    # 我的课程
    url(r'course/$', UserCourseView.as_view(), name="course"),

]

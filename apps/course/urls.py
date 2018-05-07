from django.conf.urls import url

from course.views import CourseList

urlpatterns = [
# 用户信息
    url(r'list/$', CourseList.as_view(), name='list'),

]
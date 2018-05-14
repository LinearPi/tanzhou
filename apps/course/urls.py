from django.conf.urls import url



from course.views import CourseList, CourseDetailView, LessonDetailView, BuyCourseView

urlpatterns = [
    # 课程信息
    url(r'list/$', CourseList.as_view(), name='list'),

    # 课程详情
    url(r'details/(?P<course_id>.*)$', CourseDetailView.as_view(), name='details'),

    # 目录详情
    url(r'lesson/(?P<course_id>.*)$', LessonDetailView.as_view(), name='lesson'),
    
    # 购买课程
    url(r'buy/(?P<course_id>.*)$', BuyCourseView.as_view(), name='buy'),

]

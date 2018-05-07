from django.shortcuts import render
from django.views import View
from django.db.models import Q
from course.models import CourseClass, CourseSort, Course, Lesson

from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class CourseList(View):
    def get(self, request):
        # 去除第一分类
        course_class = CourseClass.objects.all()
        course_sort = CourseSort.objects.all()
        all_course = Course.objects.all()

        # 取出第一分类的id
        class_id = request.GET.get('class_id', "")
        if class_id:
            all_course = Course.objects.filter(sort__classes_id=int(class_id))

        # 取出第二分的di
        sort_id = request.GET.get('sort_id', "")
        if sort_id:
            all_course = Course.objects.filter(sort_id=int(sort_id))

        # lesson = Lesson.objects.get(lesson_course_id=1)
        # lesson_des = lesson.lesson_course.all()
        price = request.GET.get('price', "")
        if price:
            all_course = Course.objects.filter(price=price)



        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
            # 比如对课程进行分页.
        # all_course需要分页的对象    数字 表示每页显示的数值
        p = Paginator(all_course, 4, request=request)

        all_course = p.page(page)

        return render(request, 'course_list.htm', {"course_class": course_class,
                                                   "course_sort": course_sort,
                                                   "all_course": all_course,
                                                   # "lesson_des": lesson_des,
                                                   })

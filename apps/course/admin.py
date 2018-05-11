from django.contrib import admin
from course.models import Course, CourseClass, CourseSort, Lesson, Teacher,Buy


# Register your models here.


class SortInline(admin.StackedInline):  # 第二分类
    model = CourseSort
    extra = 2


class TeacherInline(admin.StackedInline):  # 在课程下面显示章节的
    model = Teacher
    extra = 1


class CourseClassAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
    inlines = [SortInline]


class CourseSortAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


class LessonInline(admin.TabularInline):  # 在课程下面显示章节的
    model = Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "learn_time", "nums", ]
    list_filter = ["name", "price", "learn_time", "nums"]
    search_fields = ["name", "price", "learn_time", "nums"]
    inlines = [LessonInline, TeacherInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ["name", "lesson_course"]
    list_filter = ["name", "lesson_course"]
    search_fields = ["name", "lesson_course"]


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["teacher_name", "teacher_des", "teacher_course"]
    list_filter = ["teacher_name", "teacher_des", "teacher_course"]
    search_fields = ["teacher_name", "teacher_des", "teacher_course"]

class BuyAdmin(admin.ModelAdmin):
    list_display = ["user", "course", "add_time"]
    list_filter = ["user", "course", "add_time"]
    search_fields = ["user", "course", "add_time"]


admin.site.register(CourseClass, CourseClassAdmin)
admin.site.register(CourseSort, CourseSortAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Buy, BuyAdmin)





# 第二种方法 装饰器的用法
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ["name", "price", "learn_time", "nums", "image", "describe"]
#     list_filter = ["name", "price", "learn_time", "nums"]
#     search_fields = ["name", "price", "learn_time", "nums"]
#
#     class Meta():
#         verbose_name = u"课程"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name

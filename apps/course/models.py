from django.db import models

from datetime import datetime
from users.models import UserInfo


# Create your models here.

class CourseClass(models.Model):
    name = models.CharField(choices=(('it', u"IT互联网"), ('language', u'语言留学'), ('design', u'创意设计'), ('life', u'兴趣生活'),
                                     ('plant', u'生产种植'), ('edu', u'升学考研'), ('certificate', u'公培考证')),
                            max_length=15, verbose_name=u'分类')

    class Meta:
        verbose_name = u"第一分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.get_name_display()


class CourseSort(models.Model):
    classes = models.ForeignKey(CourseClass, verbose_name=u"第一分类")
    name = models.CharField(max_length=50, verbose_name=u'第二分类')

    class Meta:
        verbose_name = u"第二分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    sort = models.ForeignKey(CourseSort, verbose_name=u"分类")
    name = models.CharField(max_length=30, verbose_name=u"课程名称")
    price = models.IntegerField(default=0, verbose_name=u"价格")
    learn_time = models.CharField(max_length=6, verbose_name=u"学习时长")
    nums = models.IntegerField(default=0, verbose_name=u"购买人数")
    image = models.ImageField(upload_to="img/%Y/%m", verbose_name=u"封面图")
    describe = models.ImageField(upload_to='img/course/%Y/%m', verbose_name='描述')
    click_num = models.IntegerField(default=0, verbose_name=u"点击人数")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_buy_count(self):
        return self.buy_set.all().count()



class Lesson(models.Model):
    lesson_course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=40, verbose_name=u"课程名")
    start_time = models.DateTimeField(default=datetime.now, verbose_name=u"开始时间")
    end_time = models.DateTimeField(default=datetime.now, verbose_name=u"结束时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    teacher_course = models.ForeignKey(Course, verbose_name=u"课程名")
    teacher_name = models.CharField(max_length=30, verbose_name=u"老师名")
    teacher_des = models.CharField(max_length=100, verbose_name=u"老师描述")
    teacher_img = models.ImageField(upload_to="img/tea/&Y/%m", verbose_name=u"老师图")

    class Meta:
        verbose_name = u"老师"
        verbose_name_plural = verbose_name


class Buy(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"购买时间")

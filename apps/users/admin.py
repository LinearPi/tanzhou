from django.contrib import admin

from users.models import UserInfo


# Register your models here.


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["username", "nick_name", "birthday", "gender", "image", "phone", "qq", "summary"]
    list_filter = ["username", "nick_name", "birthday", "gender", "image", "phone", "qq", "summary"]
    search_fields = ["username", "nick_name", "birthday", "gender", "image", "phone", "qq", "summary"]

    class Meta():
        verbose_name = u"用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    fieldsets = (
        # 可以设置操作
        (u'账号信息', {
            'fields': ('username', 'nick_name', 'email')
        }),

        (u'权限', {
            'fields': ('groups', 'user_permissions')
        }),

        (u'状态', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),

        # 显示不是隐藏 classes, 样式是不是
        (u'其他信息', {
            'classes': ('collapse',),
            'fields': (
            'birthday', 'gender', 'image', 'last_login', 'date_joined', 'summary', 'first_name', 'last_name'),
        }),
    )



admin.site.register(UserInfo, UserInfoAdmin)


admin.site.site_header = '潭州课堂后台管理'
admin.site.site_title = '潭州课堂'

#
# @admin.register(UserInfo)
# class UserInfoAdmin(admin.ModelAdmin):
#     list_display =["username", "nick_name", "birthday", "gender", "image", "phone", "qq", "summary"]
#     list_filter =["username", "nick_name", "birthday", "gender", "image", "phone", "qq", "summary"]
#     search_fields = ["username", "nick_name", "birthday", "gender", "image", "phone", "qq", "summary"]
#
#     class Meta():
#         verbose_name = u"用户"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.username

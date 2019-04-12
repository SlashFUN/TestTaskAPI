from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'created', 'group')


admin.site.register(User, UserAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


admin.site.register(Group, GroupAdmin)

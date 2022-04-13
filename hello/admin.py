from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . import models
from .models import UserInfo
from .resources import UserInfoResource


admin.site.register(models.User)

class UserInfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('username','password','address','email','age','sex')
 search_fields = ('username','password','address','email','age','sex')
 date_hierarchy = 'create_date'
 resource_class = UserInfoResource

class Meta:
        model = UserInfo


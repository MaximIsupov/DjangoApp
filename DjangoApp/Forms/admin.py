from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Fakulcies, Groups, Students

@admin.register(Fakulcies)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("fakulcy_name",)
    list_filter = ("fakulcy_name",)
    search_fields = ("fakulcy_name__startswith", )

@admin.register(Groups)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_num", "fakulcy_id")
    list_filter = ("group_num", "fakulcy_id")
    search_fields = ("group_num__startswith",)

@admin.register(Students)
class FakulcyAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "group_id")
    list_filter = ("name", "surname", "group_id")
    search_fields = ("name__startswith", "surname__startswith",)



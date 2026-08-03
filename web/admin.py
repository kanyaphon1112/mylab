from django.contrib import admin
from .models import student


@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_id', 'fname', 'lname')
    search_fields = ('stu_id', 'fname', 'lname')
    ordering = ('stu_id',)

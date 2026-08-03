from django.urls import reverse
from django.db import models
from django.contrib import admin

PREFIX = [
    ("นาย", "นาย"),
    ("นางสาว", "นางสาว"),
    ("นาง", "นาง"),
]


class student(models.Model):
    prefix_name = models.CharField(max_length=100, blank=False, choices=PREFIX)
    stu_id = models.CharField(max_length=12, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.fname + " " + self.lname

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})


class StudentsAdmin(admin.ModelAdmin):
    list_display = ("stu_id", "prefix_name", "fname", "lname")


admin.site.register(student, StudentsAdmin)

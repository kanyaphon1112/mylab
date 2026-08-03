from django.urls import reverse
from django.db import models


class student(models.Model):

    stu_id = models.CharField(max_length=12, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.fname + " " + self.lname

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

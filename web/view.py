from django.shortcuts import render
from .models import student


def home(request):
    import datetime

    context = {
        "title": "My Home Page",
    }
    student = student.objects.all()
    context["student"] = student

    context["date"] = datetime.date.today()
    return render(request, "myabb/home.html", context)


def about(request):
    return render(request, "myabb/about.html")


def contact(request):
    return render(request, "myabb/contact.html")

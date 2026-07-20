from django.shortcuts import render


def home(request):
    import datetime

    context = {
        "title": "My Home Page",
    }
    context["date"] = datetime.date.today()
    return render(request, "myabb/home.html", context)


def about(request):
    return render(request, "myabb/about.html")


def contact(request):
    return render(request, "myabb/contact.html")

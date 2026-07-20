from django.shortcuts import render

def home(request):
    return render(request, 'myabb/home.html')

def about(request):
    return render(request, 'myabb/about.html')

def contact(request):
    return render(request, 'myabb/contact.html')

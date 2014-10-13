from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def wheel(request):
    return render(request, 'wheel.html')

def about(request):
    return render(request, 'about.html')
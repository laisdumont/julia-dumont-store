from django.shortcuts import render


def home(request):
    return render(request, "../templates/home.html")

def clothes(request):
    return render(request, "../templates/clothes.html")

def singUp(request):
    return render(request, "../templates/singUp.html")
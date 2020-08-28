from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    print(request.method)
    return render(request, 'index.html')


def validate(request):
    if request.method == "POST":
        pass
    else:
        redirect("/")

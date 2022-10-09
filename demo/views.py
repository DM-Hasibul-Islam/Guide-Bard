from django.shortcuts import render, HttpResponse


# Create your views here.
def homePage(request):
    # return HttpResponse("<h1>This is HomePage.</h1>")
    return render(request, 'home.html')


def sign_up(request):
    return HttpResponse("<h1>This is sign up Page.</h1>")


def login(request):
    return HttpResponse("<h1>This is login Page.</h1>")


def tourist(request):
    return HttpResponse("<h1>This is Tourist Page.</h1>")


def tourist_guide(request):
    return HttpResponse("<h1>This is Tourist Page for booking tour Guide.</h1>")


def payment(request):
    return HttpResponse("<h1>This is Tourist Page for payment.</h1>")


def tour_guide(request):
    return HttpResponse("<h1>This is Tour Guide's Page.</h1>")
    return HttpResponse("<h1>This is Tour Guide's interface.</h1>")


def emergency(request):
    return HttpResponse("<h1>This is Emergency contacts page.</h1>")

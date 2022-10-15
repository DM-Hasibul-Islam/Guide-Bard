from django.shortcuts import render, HttpResponse


# Create your views here.
def homePage(request):
    # return HttpResponse("<h1>This is HomePage.</h1>")
    dict = {
        'name': 'Anika',
        'id': 20101069,
        'email': '20101069@uap-bd.edu',
    }
    return render(request, 'home.html', dict)


def sign_up(request):
    # return HttpResponse("<h1>This is sign up Page.</h1>")
    dict = {
        'name': 'This is sign_up page'
    }
    return render(request, 'sign_up.html', dict)


def login(request):
    # return HttpResponse("<h1>This is login Page.</h1>")
    dict = {
        'name': 'This is login page'
    }
    return render(request, 'login.html', dict)


def tourist(request):
    # return HttpResponse("<h1>This is Tourist Page.</h1>")
    dict = {
        'name': 'This is Tourist page'
    }
    return render(request, 'tourist.html', dict)

#not used
def tourist_guide(request):
    # return HttpResponse("<h1>This is Tourist Page for booking tour Guide.</h1")
    dict = {
        'name': 'This is Tourist_Guide page'
    }

    return render(request, 'home.html', dict)


def payment(request):
    # return HttpResponse("<h1>This is Tourist Page for payment.</h1>")
    dict = {
        'name': 'This is payment page'
    }
    return render(request, 'payment.html', dict)


def tour_guide(request):
    # return HttpResponse("<h1>This is Tour Guide's Page.</h1>")
    # return HttpResponse("<h1>This is Tour Guide's interface.</h1>")
    dict = {
        'name': 'This is Tour_Guide page'
    }
    return render(request, 'tour_guide.html', dict)


def emergency(request):
    # return HttpResponse("<h1>This is Emergency contacts page.</h1>")
    dict = {
        'name': 'This is Emergency page'
    }
    return render(request, 'emergency.html', dict)


def contact(request):
    return render(request)

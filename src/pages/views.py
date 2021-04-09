from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
   # return HttpResponse("<h1>Hello World</h1>")  # string of html code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is aboutme ",
        "my_number": 1234,
        "this_is_true": True,
        "my_lists": [123, 456, 321, 'ABC'],
        "my_html": "<h1>Hello World</h1>"

    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")

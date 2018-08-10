from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, word. You'r at the polls index.")

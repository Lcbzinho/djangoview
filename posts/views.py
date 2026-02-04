from django.http import HttpResponse


def Post(request):
    return HttpResponse("hello world")

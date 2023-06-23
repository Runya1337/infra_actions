from django.http import HttpResponse


def index(request):
    return HttpResponse("Прием прием")


def second_page(request):
    return HttpResponse("Дубль 2")

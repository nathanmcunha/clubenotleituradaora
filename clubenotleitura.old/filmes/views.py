from django.shortcuts import render


def index():
    return HttpResponse("Hello World")
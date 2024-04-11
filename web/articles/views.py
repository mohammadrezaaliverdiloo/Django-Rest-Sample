from django.shortcuts import render,HttpResponse

def hello(request):
    return HttpResponse("<h1>hello</h1>")

def hello2(request):
    return HttpResponse("<h1>hello2</h1>")
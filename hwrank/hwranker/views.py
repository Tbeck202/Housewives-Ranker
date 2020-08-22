from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'hwranker/home.html')


def rhony(request):
    return render(request, 'hwranker/rhony.html')


def rhonj(request):
    return HttpResponse('<h1>This will be the RHONJ page</h1>')


def rhobh(request):
    return HttpResponse('<h1>This will be the RHOBH page</h1>')


def rhoa(request):
    return HttpResponse('<h1>This will be the RHOA page</h1>')


def rhop(request):
    return HttpResponse('<h1>This will be the RHOP page</h1>')


def rhoc(request):
    return HttpResponse('<h1>This will be the RHOC page</h1>')


def rhosl(request):
    return HttpResponse('<h1>This will be the RHOSL page</h1>')


def rhod(request):
    return HttpResponse('<h1>This will be the RHOD page</h1>')

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sayHello(request):
 return HttpResponse('Hello reservation World')
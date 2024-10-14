from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response

def say_hello(request):
    #pull data from db
    #send email
    return render(request, 'hello.html',{'name': 'Mosh'} )


def second_exp(request):
    return HttpResponse('second expression')


import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


# function base view
def home(request):
    num = random.randint(0, 2000000)
    some_list = [num , random.randint(0, 2000000) , num]
    context = {
        'bool_var': True,
        'num': num,
        'some_list' : some_list,
    }
    return render(request,'home.html', context )

def home2(request):
    context = {}
    return render(request,'home2.html', context )

def home3(request):
    context = {}
    return render(request,'home3.html', context )

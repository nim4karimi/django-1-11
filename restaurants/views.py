import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

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

def contact(request):
    context = {}
    return render(request,'contact.html', context )

def about(request):
    context = {}
    return render(request,'about.html', context )


class ContactView(View):
    def get(self, request):
        context = {}
        return render(request, 'contact.html', context)
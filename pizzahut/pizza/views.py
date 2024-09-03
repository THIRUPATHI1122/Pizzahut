from django.shortcuts import render
from .forms import PizzaForm

# Create your views here.

def homepage(request):
    return render(request,'pizza/home.html')


def order(request):
    form =PizzaForm()    #empty form
    return render(request,'pizza/order.html',{'pizzform':form})



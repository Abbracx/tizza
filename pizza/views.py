from django.shortcuts import render
from django.http import HttpResponse
from pizza.models import Pizza

# Create your views here.
def index(request, pid):
    pizza = Pizza.objects.get(id=pid)
    return HttpResponse(pizza)



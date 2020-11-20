from pizzaria.models import Pizza
from django.shortcuts import render

def index(request):

    pizzas = Pizza.objects.all()
    dados = {
        'pizzas' : pizzas
    }
    return render(request,'index.html',dados)
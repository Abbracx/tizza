from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from pizza.models import Pizza
from django.contrib.auth.decorators import login_required
import json



@login_required
def index(request, pid):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_pizza = Pizza.objects.create(
            title=data['title'],
            description=data['description'],
            creator=request.user,
        )

        new_pizza.save()
        return HttpResponse(new_pizza)

    elif request.method == "GET":
        pizza = Pizza.objects.get(id=pid)
        return HttpResponse(pizza)
    


class GetTenPizza(View):
    template_name = 'ten_pizza.html'

    def get(self, request):
        pizzas = Pizza.objects.order_by('?')[:10]
        return render(request, self.template_name, {'pizzas': pizzas})

    
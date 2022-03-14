from django.contrib import admin
from pizza.models import Pizzeria, Pizza, Likes

# Register your models here.

@admin.register(Pizzeria)
class PizzeriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    pass
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Pizzeria(models.Model):
    owner   = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone   = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.owner} Pizzaz'



class Pizza(models.Model):
    CHOICES = (
        ('meat','meat'),
        ('vegan','vegan'),
    )
    title       = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    thumbnail_url   = models.URLField()
    approved    = models.BooleanField(default=False)
    toppings    = models.CharField(max_length=10, choices=CHOICES, default=CHOICES[0])
    creator     = models.ForeignKey(Pizzeria, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

from django.db import models

from shared.finances import Currency


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    price = models.IntegerField()
    currency = models.CharField(max_length=3, default=Currency.USD)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.price} {self.currency}"

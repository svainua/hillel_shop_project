import enum
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Status(enum.StrEnum):
    PENDING = enum.auto()
    COMPLETED = enum.auto()
    CANCELLED = enum.auto()


class Order(models.Model):
    # null only to avoid authentication
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    number = models.UUIDField(default=uuid.uuid4, unique=True)

    status = models.CharField(max_length=15, default=Status.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}: {self.created_at}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        "orders.Order", on_delete=models.CASCADE, related_name="items"
    )
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    # total_price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product}: {self.quantity}"


# OrderItem.objects.get(id=13).product
# OrderItem.objects.get(id=13).items.all() items позволяет получить все элементы, которые входят в этот запрос благодаря related_name #noqa

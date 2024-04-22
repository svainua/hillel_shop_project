from django.shortcuts import get_object_or_404
from rest_framework import permissions, serializers, viewsets  # noqa
from rest_framework.decorators import action, api_view, permission_classes  # noqa
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Order


class OrderItemProductSerializer(serializers.Serializer):
    price = serializers.IntegerField()
    currency = serializers.CharField()


class OrderItemLightSerializer(serializers.Serializer):
    product = OrderItemProductSerializer(read_only=True)
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class OrderSerializer(serializers.Serializer):
    user = serializers.IntegerField(read_only=True)
    number = serializers.UUIDField(read_only=True)
    status = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    items = OrderItemLightSerializer(read_only=True, many=True)


class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True


def _orders_create(request: Request):
    serializer = OrderSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.validated_data)


def _orders_list():
    queryset = Order.objects.all()
    serializer = OrderSerializer(queryset, many=True)

    return Response(serializer.data)


@api_view(http_method_names=["get", "post"])
@permission_classes([MyCustomPermission])
def orders_list_create(request: Request):
    if request.method == "POST":
        return _orders_create(request)
    else:
        return _orders_list()


@api_view(http_method_names=["get"])
@permission_classes([MyCustomPermission])
def orders_retrieve(request: Request, id: int):
    order = get_object_or_404(Order, id=id)
    serializer = OrderSerializer(order)

    return Response(serializer.data)

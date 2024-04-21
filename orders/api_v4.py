from django.shortcuts import get_object_or_404
from rest_framework import permissions, serializers, viewsets
from rest_framework.decorators import action
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


class OrdersAPISetV2(viewsets.ViewSet):
    @action(methods=["get"], detail=False)
    def fetch_all_orders(self, request: Request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)

        return Response(serializer.data)

    @action(methods=["post"], detail=False, permission_classes=[MyCustomPermission])
    def create_order(self, request: Request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data)

    @action(methods=["get"], detail=True)
    def retrieve_order(self, request: Request, id: int):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order)

        return Response(serializer.data)

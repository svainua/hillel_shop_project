from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
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


class OrdersAPISet(viewsets.ViewSet):
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data)

    def retrieve(self, request, id: int):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order)

        return Response(serializer.data)

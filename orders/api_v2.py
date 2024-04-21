from rest_framework import generics, serializers

from .models import Order, OrderItem


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


class OrderListCreateAPI(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "id"


class OrderItemListCreateAPI(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemLightSerializer


class OrderItemRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemLightSerializer
    lookup_url_kwarg = "id"

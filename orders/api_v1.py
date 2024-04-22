from rest_framework import generics, serializers

from .models import Order, OrderItem


class OrderItemProductSerializer(serializers.Serializer):
    price = serializers.IntegerField()
    currency = serializers.CharField()


class OrderItemLightSerializer(serializers.ModelSerializer):
    product = OrderItemProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemLightSerializer(
        read_only=True, many=True
    )  # many - применяет к одному объекту или к многим. Возвращает либо список просериализованных объектов, либо сам объект,если many не указан #noqa

    class Meta:
        model = Order
        fields = "__all__"


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


# class OrderItemProductSerializer(serializers.Serializer):
#     price = serializers.IntegerField()
#     currency = serializers.CharField()


# class OrderItemLightSerializer(serializers.ModelSerializer):
#     product = OrderItemProductSerializer(read_only=True)

#     class Meta:
#         model = OrderItem
#         fields = "__all__"


# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemLightSerializer(read_only=True, many=True)

#     class Meta:
#         model = Order
#         fields = "__all__"


# class OrderListCreateAPI(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# class OrderRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     lookup_url_kwarg = "id"


# class OrderItemListCreateAPI(generics.ListCreateAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemLightSerializer


# class OrderItemRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = OrderItem.objects.all()
#     # serializer_class = OrderItemLightSerializer
#     lookup_url_kwarg = "id"

from django.urls import path
from rest_framework.routers import DefaultRouter  # noqa

from orders.api_v1 import (
    OrderItemListCreateAPI,
    OrderListCreateAPI,
    OrderRetrieveUpdateDeleteAPI,
)
from orders.api_v5 import orders_list_create, orders_retrieve  # noqa
from products.api import ProductListCreateAPI, ProductRetrieveUpdateDeleteAPI

# from orders.api_v4 import OrdersAPISetV2


# from orders.api_v3 import OrdersAPISet


# from orders.api_v2 import (
#     OrderItemListCreateAPI,
#     OrderListCreateAPI,
#     OrderRetrieveUpdateDeleteAPI,
# )


# V2
urlpatterns = [
    path(
        "products/",
        ProductListCreateAPI.as_view(),
    ),
    path(
        "products/<int:id>/",
        ProductRetrieveUpdateDeleteAPI.as_view(),
    ),
    path(
        "orders/",
        OrderListCreateAPI.as_view(),
    ),
    path(
        "orders/<int:id>/",
        OrderRetrieveUpdateDeleteAPI.as_view(),
    ),
    path(
        "orders/items/",
        OrderItemListCreateAPI.as_view(),
    ),
]

# V3
# urlpatterns = [
#     path(
#         "orders/",
#         OrdersAPISet.as_view(
#             {
#                 "get": "list",
#                 "post": "create",
#             },
#         ),
#     ),
#     path(
#         "orders/<int:id>",
#         OrdersAPISet.as_view(
#             {
#                 "get": "retrieve",
#             },
#         ),
#     ),
# ]

# V4
# urlpatterns = []

# it could be imported from the ``orders.router.py``  ¯\_(ツ)_/¯
# orders_router = DefaultRouter()
# orders_router.register("orders", OrdersAPISetV2, basename="order")

# urlpatterns += orders_router.urls


# V5
# urlpatterns = [
#     path("orders/", orders_list_create),
#     path("orders/<int:id>/", orders_retrieve),
# ]

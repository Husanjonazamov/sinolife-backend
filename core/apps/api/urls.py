from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    ProductView,
    CategoryView,
    BannerView, CartView, OrderView, CartitemView, OrderitemView,
    ContactView, MessagesView
)

from core.apps.api.views import ProductSearchAPIView

router = DefaultRouter()
router.register(r"product", ProductView, basename="product")
router.register(r"category", CategoryView, basename="category")
router.register(r"banner", BannerView, basename="banner")
router.register(r"cart", CartView, basename="cart")
router.register(r"order", OrderView, basename="order")
router.register(r"cart-item", CartitemView, basename="cart-item")
router.register(r"contact", ContactView, basename="contact")
router.register(r"message", MessagesView, basename="message")
router.register(r"order-item", OrderitemView, basename="order-item")

urlpatterns = [
    path("", include(router.urls)),
    path("product/", ProductSearchAPIView.as_view(), name="product_search")
]

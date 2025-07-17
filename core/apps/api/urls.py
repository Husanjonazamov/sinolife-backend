from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    ProductView,
    CategoryView,
    BannerView, CartView, OrderView
)

router = DefaultRouter()
router.register(r"product", ProductView, basename="product")
router.register(r"category", CategoryView, basename="category")
router.register(r"banner", BannerView, basename="banner")
router.register(r"cart", CartView, basename="cart")
router.register(r"order", OrderView, basename="order")


urlpatterns = [
    path("", include(router.urls)),
]

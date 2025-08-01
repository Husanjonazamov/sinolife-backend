"""
Accounts app urls
"""

from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import RegisterView, ResetPasswordView, MeView, ChangePasswordView
from rest_framework.routers import DefaultRouter
from core.apps.accounts.views.login import MyTokenObtainPairView
# from core.apps.accounts.views.tg_auth import TgRegisterView

router = DefaultRouter()
router.register("auth", RegisterView, basename="auth")
router.register("auth", ResetPasswordView, basename="reset-password")
router.register("auth", MeView, basename="me")
router.register("auth", ChangePasswordView, basename="change-password")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
    path(
        "auth/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",   
    ),
    
    # tg register
    # path("user/create/", TgRegisterView.as_view(), name="user-create")
]

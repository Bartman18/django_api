from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter

from . import views as v

router = DefaultRouter()
router.register(r'products', v.ProductViewSet, basename='product')
router.register(r'reservations', v.ReservationViewSet, basename='reservation')
router.register(r'orders', v.OrderViewSet, basename='order')


urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', v.CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', v.RegisterView.as_view(), name='register'),
    # path('login/', v.LoginView.as_view(), name='login'),
    path('user/', v.ProfileView.as_view(), name='user'),
    path('', include(router.urls)),





]
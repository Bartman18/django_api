from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter

from . import views as v

router = DefaultRouter()
router.register(r'products', v.ProductViewSet, basename='product')


urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path( 'token/refresh/', v.CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', v.RegisterView.as_view(), name='register'),
    path('login/', v.LoginView.as_view(), name='login'),
    # path('logout/', v.LogoutView.as_view(), name='logout'),
    # path('add_product/', v.ProductAddView.as_view(), name='add_product'),
    #
    # path('edit_product/', v.ProductUpdateView.as_view(), name='edit_product'),
    # path('delete_product/', v.ProductDeleteView.as_view(), name='delete_product'),
    #
    # path('show_product/', v.ProductListView.as_view(), name='show_product')




]
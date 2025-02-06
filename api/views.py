
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status, viewsets
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAdminUser, AllowAny
import datetime
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenRefreshView

from .models import Product, Order
# from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, ProductSerializer, OrderSerializer, ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken



User = get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()


            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "message": "User created successfully",
                "user": serializer.data,
                "access": access_token,
                "refresh": str(refresh)
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']


            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "message": "User logged in successfully",
                "access": access_token,
                "refresh": str(refresh)
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         try:
#             refresh_token = request.data.get("refresh")
#             if not refresh_token:
#                 return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
#
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#
#             return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
#         except TokenError:
#             return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateAPIView):

    queryset =User.objects.all()
    serializer_class = ProfileSerializer

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            response.data['message'] = "Token refreshed successfully"
            response.data['user'] = {
                "username": request.user.username,
                "email": request.user.email,
            }

        return response



# class ProductAddView(generics.CreateAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductListView(generics.ListAPIView):
#     permission_classes = [AllowAny]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductUpdateView(generics.RetrieveUpdateAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = "pk"
#
# class ProductDeleteView(generics.DestroyAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = "pk"  # DRF
#
#     def destroy(self, request, *args, **kwargs):
#         product = self.get_object()
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)




class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        order = Order.objects.filter(id=order_id,
                                     user=request.user).first()

        if not order:
            return Response({"error": "You can't delete your order after 30 minutes."},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

        now_time = timezone.now()
        if now_time - order.date_ordered >= timezone.timedelta(minutes=30):
            return Response({"error": "You can't delete you order"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

        order.delete()
        return Response({"message": "Order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):

        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    @action(detail=False, methods=['GET'])
    def my_orders(self, request):

        orders = self.get_queryset()
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)




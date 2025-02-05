
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAdminUser, AllowAny


from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenRefreshView

from .models import Product, Order

from .serializers import RegisterSerializer, LoginSerializer, ProductSerializer, OrderSerializer
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



class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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



class ProductAddView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

class ProductDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # DRF

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






# class OrderCreateView(generics.CreateAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
# class OrderDestroyView(generics.DestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
#     permission_classes = [permissions.IsAuthenticated]
#     def destroy(self, request, *args, **kwargs):
#
#         order = self.get_object()
#         order.delete()

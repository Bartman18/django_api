
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from rest_framework_simplejwt.exceptions import TokenError

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Product
# from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, ProductSerializer
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


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

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






class ProductAddView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


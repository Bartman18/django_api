from contextvars import Token
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
# from api.models import User
from django.contrib.auth import get_user_model

from api.models import Product, Order

User = get_user_model()  # Use the custom user model

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 as it's not in the User model
        validated_data['password'] = make_password(validated_data['password'])  # Hash the password
        user = User.objects.create(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError({"email": "Invalid email or password."})

        if not user.is_active:
            raise serializers.ValidationError({"email": "This account is inactive."})

        data['user'] = user
        return data




class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']



class OrderSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    product_name = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = Order
        fields = ['id', 'user', 'user_email', 'product', 'product_name', 'quantity', 'price', 'date_ordered']


    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        validated_data['user'] = user
        return super().create(validated_data)

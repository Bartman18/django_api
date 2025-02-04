from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.email
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

class WashingType(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return f"Washing Type: {self.name} Price: {self.price}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_id = models.ForeignKey(WashingType, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return f"Reservation #{self.reservation_id} ({self.type_id}) by {self.user.username} on {self.date}"




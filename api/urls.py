from django.urls import path
import views as v

urlpatterns = [
    path('register/', v.RegisterView.as_view(), name='register'),
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
    path('add_product/',v.ProductAddView.as_view(), name='add_product'),

    path('edit_product/', v.ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/', v.ProductDeleteView.as_view(), name='delete_product'),



]
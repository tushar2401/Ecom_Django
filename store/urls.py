from django.contrib import admin
from django.urls import path
from .views import index,signup,login,cart,checkout,orders
from .middlewares.auth import auth_middleware
urlpatterns = [
    path('',index.Index.as_view() ,name='index'),
    path('signup',signup.Signup.as_view(),name='signup'),
    path('login',login.Login.as_view(),name='login'),
    path('logout',login.logout,name='logout'),
    path('cart',cart.Cart.as_view(),name='cart'),
    path('check-out',checkout.CheckOut.as_view(),name='checkout'),
    path('orders', auth_middleware(orders.OrderView.as_view()), name='orders'),
]

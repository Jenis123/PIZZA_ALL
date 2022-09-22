"""PIZZA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pizza_app import views
urlpatterns = [

    # path('home/', views.home, name='home'),
    path('increment/<int:pk>/', views.increment, name='increment'),
    # path('reset/', views.reset, name='reset'),
    path('decrement/<int:pk>/', views.decrement, name='decrement'),
    path('customer_registration/', views.customer_registration, name='customer_registration'),
    path('customer_wlc/', views.customer_wlc, name='customer_wlc'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('addpizza/', views.add_pizza, name='add_pizza'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit_pizza/<int:pk>/', views.edit_pizza, name='edit_pizza'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/', views.order, name='order'),
    path('myorder/', views.myorder, name='myorder'),
    path('adminshoworder/', views.adminshoworder, name='adminshoworder'),
    path('pizza_delete_checkout/<int:pk>/', views.pizza_delete_checkout, name='pizza_delete_checkout'),
    path('reject_order/<int:pk>/', views.reject_order, name='reject_order'),
    path('accept_order/<int:pk>/', views.accept_order, name='accept_order'),
 ]

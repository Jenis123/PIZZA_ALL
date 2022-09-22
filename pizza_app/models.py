from asyncio.base_futures import _PENDING
from lzma import MODE_FAST
from django.db import models


# Create your models here.
class CountNum(models.Model):
    countnum=models.CharField(max_length=10)



class Menu(models.Model):
    pizza_name=models.CharField(max_length=200)
    pizza_price=models.CharField(max_length=200)
    pizza_image=models.FileField()

    def __str__ (self):
        return self.pizza_name

class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=50)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=10)

    def __str__ (self):
        return self.first_name


class Order(models.Model):
    menu_id = models.ForeignKey(Menu,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField(default=0)
    total_price=models.CharField(max_length=50)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    status = models.CharField( max_length=200 ,default="PENDING")

    def __str__ (self):
        return self.menu_id.pizza_name

class Cart(models.Model):
    menu_id = models.ForeignKey(Menu,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)

class MyCart(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField(default=0)
    total_price=models.IntegerField(default=0)
	
    def __str__ (self):
        return self.menu_id.pizza_name


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Brand(models.Model):
    name=models.CharField(max_length=200,unique=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

    


class Bikes(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=200,null=True)
    brand_object=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="cart")
    year=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    image=models.ImageField(upload_to="bike_images",default="default.jpg",null=True,blank=True)
    cubic_capacity=models.CharField(max_length=200)
    distance_travelled=models.CharField(max_length=200)
    ownership=models.CharField(max_length=200,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    



class Favourites(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    @property
    def cart_items(self):
        return self.cartitem




class FavouriteItem(models.Model):
    Bikes_object=models.ForeignKey(Bikes,on_delete=models.CASCADE)
    Favourite_object=models.ForeignKey(Favourites,on_delete=models.CASCADE,related_name="cartitem")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    is_order_placed = models.BooleanField(default=False,null=True)
    is_active=models.BooleanField(default=True)
    



def create_basket(sender,instance,created,**kwargs):

    if created:
        Favourites.objects.create(owner=instance)

post_save.connect(create_basket,sender=User)




class Order(models.Model):

    user_object=models.ForeignKey(User,on_delete=models.CASCADE,related_name="purchase")
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=200,null=True)
    is_paid=models.BooleanField(default=False)
    order_id=models.CharField(max_length=200,null=True)
    option=(
        ("booked","booked"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=option,default="booked")

    @property
    def get_order_items(self):
        return self.purchaseitems.all()    



class OrderItems(models.Model):
    order_object=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="purchaseitems")
    basket_item_object=models.ForeignKey(FavouriteItem,on_delete=models.CASCADE)
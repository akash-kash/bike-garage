from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView
from store.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from store.models import Bikes,FavouriteItem,Order,OrderItems

# Create your views here.



class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"data":form})
   
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        return render(request,"login.html",{"data":form})
  


class SignInView(View):
    def get(slef,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"data":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=u_name,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("index")
        messages.error(request,"invalid credentials")
        return render(request,"login.html",{"data":form})
   
           
   

class IndexView(View):
    def get(self,request,*args,**kwargs):
        qs=Bikes.objects.all()
        return render(request,"index.html",{"data":qs})
    

class AboutUsView(View):
   def get(self,request,*args,**kwargs):
       return render(request,"about.html")
    



class AddToCarttView(View):
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        bike_object=Bikes.objects.get(id=id)
        FavouriteItem.objects.create(
            Bikes_object=bike_object,
            Favourite_object=request.user.cart   
        )
        return redirect("index")
    

class BikesDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        gs=Bikes.objects.get(id=id)
        return render(request,"detail.html",{"data":gs})




class CartListView(View):
    def get(self,request,*args,**kwargs):
        qs=request.user.cart.cartitem.all()
        return render(request,"cartlist.html",{"data":qs})
    


class FavouriteItemRemoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        FavouriteItem.objects.get(id=id).delete()
       
        return redirect("cart-list")
    


class CheckoutView(View):
    
    def get(self,request,*args,**kwargs):

        return render(request,"checkout.html")


    def post(self,request,*args,**kwargs):

        email=request.POST.get("email")
        phone=request.POST.get("phone")


        order_obj=Order.objects.create(
            user_object=request.user,
            phone=phone,
            email=email,
        )
        try:
            favorite_items=request.user.cart.cart_items


            for bi in favorite_items:
                OrderItems.objects.create(
                    order_object=order_obj,
                    basket_item_object=bi
                )
                bi.is_order_placed=True
                bi.save()

        except:
            order_obj.delete()

        finally:
            return redirect("index")



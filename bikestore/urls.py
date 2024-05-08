"""
URL configuration for bikestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("registration/",views.RegistrationView.as_view(),name="signup"),
    path("signin/",views.SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("detail/<int:pk>/",views.BikesDetailView.as_view(),name="bikes-detail"),
    path("basket/<int:pk>/add-to-basket/",views.AddToCarttView.as_view(),name="addTo-basket"),
    path("basket/items/all/",views.CartListView.as_view(),name="cart-list"),
    path("basket/remove/<int:pk>/",views.FavouriteItemRemoveView.as_view(),name="item-remove"),
    path('about/',views.AboutUsView.as_view(),name="about-us"),
    path('checkout/',views.CheckoutView.as_view(),name="check-out")
    

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

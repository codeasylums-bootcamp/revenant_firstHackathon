# django imports
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# restframework imports
from rest_framework import routers


# app level imports 
from shopchoice.views import FlipkartView

router = routers.DefaultRouter()

router.register(r'flipkart', FlipkartView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('shopchoice/',include('shopchoice.urls')),

]
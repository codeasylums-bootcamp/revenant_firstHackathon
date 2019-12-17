# django imports
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# app level imports
from shopchoice import views

urlpatterns = [
    #path('func_view/', views.func_view),
    path('', views.search,name='search'),
    #path('search1/', views.search1,name='search1'),
    path("search1",views.search1,name='search1')
   


]
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from shopchoice.models import flipkart
from shopchoice.serializers import CartSerializer

# Create your views here.
#@csrf_exempt 



#class class_view(View):

    #def get(self, request):
    #    return HttpResponse("Class based")

def search(request):
    return render(request,'shopchoice/index.html')


def search1(request):
 
    #lf=request.POST['search']
    #v=request.POST['search']

    return render(request,'shopchoice/index1.html')


class FlipkartView(viewsets.ModelViewSet):
    queryset = flipkart.objects.all()
    serializer_class=CartSerializer

    @action(methods=['get'], detail=False, url_path="products")
    def products(self, request):
        products= flipkart.objects.all()
        serializer=CartSerializer(data=products)
        #query=request.get()
        if serializer.is_valid():
        #for i in range(len(products)):
            if query in products[i].split():
               ls=[products[i].prod_brand,products[i].prod_name,products[i].price,products[i].prod_discount]
            return ls
            #return Response(status.HTTP_302_FOUND)
        else:
            return Response(status.HTTP_204_NO_CONTENT)

        
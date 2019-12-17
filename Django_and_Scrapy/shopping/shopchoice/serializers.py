from rest_framework import serializers

from shopchoice.models import flipkart,ajio
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=flipkart
        fields='_all_'
        fields=['prod_brand','prod_name','prod_price','prod_discount']
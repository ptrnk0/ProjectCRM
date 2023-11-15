from rest_framework import serializers
from clientapp.models import Client
from decimal import Decimal

# class ClientSerializer(serializers.ModelSerializer):
#     cell_phone = serializers.IntegerField(source='phone')
#     price_after_calculate = serializers.SerializerMethodField(method_name = 'calculate_price')
#     class Meta:
#         model = Client
#         fields = ['id', 'first_name', 'last_name', 'price_after_calculate', 'cell_phone', 'email', 'birthday', 'comment']

#     def calculate_price(self, product:Client):
#         return product.email * Decimal(1.1)


# class  ClientSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField(max_length=15)
#     last_name = serializers.CharField(max_length=15)

class ClientSerializer(serializers.ModelSerializer):
    cell_phone = serializers.CharField(source='phone')
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'cell_phone', 'email', 'birthday', 'comment']
from dataclasses import fields
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class ProductListSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ["id","category","name","quantity","um","purchase_price","sale_price"]
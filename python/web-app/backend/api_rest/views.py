from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Order, OrderItem
from .serializer import ProductSerializer, OrderSerializer

import json

# Create your views here.

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_orders(request):
    if request.method == 'GET':
        orders = Order.objects.all().order_by('-order_date')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order(request): 
    items_data = request.data.get("items")

    if not items_data:
        return Response({"error": "Items are required"}, status=status.HTTP_400_BAD_REQUEST)

    order = Order.objects.create()

    for item in items_data:
        try:
            product = Product.objects.get(id=item["product_id"])
        except Product.DoesNotExist:
            return Response({"error": f"Product {item['product_id']} not found"}, status=status.HTTP_404_NOT_FOUND)

        quantity = item.get("quantity", 1)

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price_at_order=product.price
        )

    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
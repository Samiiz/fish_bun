from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, SalesItem, SalesRecord
from .serializers import (ProductSerializer, SalesItemSerializer,
                          SalesRecordSerializer)


# Create your views here.
class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)


class SaleRecordView(APIView):
    def get(self, request):
        record = SalesRecord.objects.all()
        serializer = SalesRecordSerializer(record, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        record = SalesRecordSerializer(data=request.data)
        if record.is_valid():
            record.save()
            return Response(record.data, status=status.HTTP_201_CREATED)
        return Response(record.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesItemView(APIView):
    def get(self, request):
        item = SalesItem.objects.all()
        serializer = SalesItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        item = SalesItemSerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(item.data, status=status.HTTP_201_CREATED)
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OrderRecord, RawMaterial, Stock, Supplier
from .seralizers import (OrderRecordSerializer, RawMaterialSerializer,
                         StockSerializer, SupplierSerializer)


# Create your views here.
class OrderRecordView(APIView):
    def get(self, request):
        records = OrderRecord.objects.all()
        serializer = OrderRecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        record = OrderRecordSerializer(data=request.data)
        if record.is_valid():
            record.save()
            return Response(record.data, status=status.HTTP_201_CREATED)
        return Response(record.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierView(APIView):
    def get(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        supplier = SupplierSerializer(data=request.data)
        if supplier.is_valid():
            supplier.save()
            return Response(supplier.data, status=status.HTTP_201_CREATED)
        return Response(supplier.errors, status=status.HTTP_400_BAD_REQUEST)


class RawMaterialView(APIView):
    def get(self, request):
        raw_materials = RawMaterial.objects.all()
        serializer = RawMaterialSerializer(raw_materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        raw_material = RawMaterialSerializer(data=request.data)
        if raw_material.is_valid():
            raw_material.save()
            return Response(raw_material.data, status=status.HTTP_201_CREATED)
        return Response(raw_material.errors, status=status.HTTP_400_BAD_REQUEST)


class StockView(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        stock = StockSerializer(data=request.data)
        if stock.is_valid():
            stock.save()
            return Response(stock.data, status=status.HTTP_201_CREATED)
        return Response(stock.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import ProductImageSerializer, MyModelSerializer
from app.models import (
    Category,
    SubCategory,
    Main,
    Partners,
    Partners_logo,
    Advert,
    News,
    News_add,
    Xaridordan_savol,
    Company,
    Contact,
    Brend,
    Product_info,
    Xarakteristika,
    Opesaniya,
    FeedBack,
    Savol_Javoblar,
    Product,
    Product_images
)


# class Products(GenericAPIView):
#     serializer_class = ProductsSerializer
#
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = self.get_serializer(products, many=True).data
#         return Response({'Success': serializer})

class Products(GenericAPIView):
    serializer_class = MyModelSerializer

    def get(self, request):
        products = Product.objects.all()
        serializer = self.get_serializer(products, many=True).data
        return Response({'Success': serializer})

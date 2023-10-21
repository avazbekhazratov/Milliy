from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import  MyModelSerializer
from app.models import (
    Product,
)


class ProductView(GenericAPIView):
    serializer_class = MyModelSerializer

    def get(self, request, pk=None):
        if pk:
            prod = Product.objects.filter(id=pk).first()
            if prod:
                ser = self.get_serializer(prod).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        prods = Product.objects.all()
        ser = self.get_serializer(prods, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "title" not in data or not data['title']:
            return Response({"Error": "Not Found"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "title" not in data or not data['title']:
            return Response({"Error": "Not Found"})

        prod = Product.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=prod)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        prod = Product.objects.filter(id=pk).first()
        if not prod:
            return Response({'Error': 'Not Found'})
        prod.delete()
        return Response({"Success": "Product Deleted"})
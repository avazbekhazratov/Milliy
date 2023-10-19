from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import CategorySerializer, SubCategorySerializer
from app.models import (
    Category,
    SubCategory,
)


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request, pk=None):
        if pk:
            ctg = Category.objects.filter(id=pk).first()
            if ctg:
                ser = self.get_serializer(ctg).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        ctgs = Category.objects.all()
        ser = self.get_serializer(ctgs, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "name" not in data or not data['name']:
            return Response({"Error": "Not Found"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "name" not in data or not data['name']:
            return Response({"Error": "Not Found"})

        ctg = Category.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=ctg)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        ctg = Category.objects.filter(id=pk).first()
        if not ctg:
            return Response({'Error': 'Not Found'})
        ctg.delete()
        return Response({"Success": "Category Deleted"})


class SubCategoryView(GenericAPIView):
    serializer_class = SubCategorySerializer

    def get(self, request, pk=None):
        if pk:
            ctg = SubCategory.objects.filter(id=pk).first()
            if ctg:
                ser = self.get_serializer(ctg).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        ctgs = SubCategory.objects.all()
        ser = self.get_serializer(ctgs, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "name" not in data or not data['name']:
            return Response({"Error": "Not Found"})

        if "subctg" not in data or not data['subctg']:
            return Response({"Error": "Not Found SubCategory"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "name" not in data or not data['name']:
            return Response({"Error": "Not Found"})
        if "subctg" not in data or not data['subctg']:
            return Response({"Error": "Not Found SubCategory"})

        ctg = SubCategory.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=ctg)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        ctg = SubCategory.objects.filter(id=pk).first()
        if not ctg:
            return Response({'Error': 'Not Found'})
        ctg.delete()
        return Response({"Success": "Category Deleted"})

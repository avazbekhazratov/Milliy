from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import  Product_info_Ser
from app.models import Product_info


class XaridorView(GenericAPIView):
    serializer_class = Product_info_Ser

    def get(self, request, pk=None):
        if pk:
            main = Product_info.objects.filter(id=pk).first()
            if main:
                ser = self.get_serializer(main).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        mains = Product_info.objects.all()
        ser = self.get_serializer(mains, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "brend" not in data or not data['brend']:
            return Response({"Error": "Data to`liq emas "})
        if "model" not in data or not data['model']:
            return Response({"Error": "Data to`liq emas"})
        if "sert" not in data or not data['sert']:
            return Response({"Error": "Data to`liq emas "})
        if "product_name" not in data or not data['product_name']:
            return Response({"Error": "Data to`liq emas"})


        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "brend" not in data or not data['brend']:
            return Response({"Error": "Data to`liq emas "})
        if "model" not in data or not data['model']:
            return Response({"Error": "Data to`liq emas"})
        if "sert" not in data or not data['sert']:
            return Response({"Error": "Data to`liq emas "})
        if "product_name" not in data or not data['product_name']:
            return Response({"Error": "Data to`liq emas"})

        main = Product_info.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=main)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        main = Product_info.objects.filter(id=pk).first()
        if not main:
            return Response({'Error': 'Not Found'})
        main.delete()
        return Response({"Success": "Category Deleted"})



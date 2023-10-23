from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import MyModelSerializer
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
            return Response({'Error': "Product not Found"})
        prods = Product.objects.all()
        ser = self.get_serializer(prods, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data

        if "product" not in data or not data['product']:
            return Response({"Error": "product not Found"})
        if "xaraktristika" not in data or not data['xaraktristika']:
            return Response({"Error": "xaraktristika not Found"})
        if "opesaniya" not in data or not data['opesaniya']:
            return Response({"Error": "opesaniya not Found"})
        if "vapros" not in data or not data['vapros']:
            return Response({"Error": "vapros not Found"})
        if "img" not in data or not data['img']:
            return Response({"Error": "product not Found"})
        if "title" not in data or not data['title']:
            return Response({"Error": "title not Found"})
        if "shop_name" not in data or not data['shop_name']:
            return Response({"Error": "shop_name not Found"})
        if "desc" not in data or not data['desc']:
            return Response({"Error": "desc not Found"})
        if "color" not in data or not data['color']:
            return Response({"Error": "color not Found"})
        if "quent" not in data or not data['quent']:
            return Response({"Error": "quent not Found"})
        if "memory" not in data or not data['memory']:
            return Response({"Error": "memory not Found"})
        if "price" not in data or not data['price']:
            return Response({"Error": "price not Found"})
        if "disc_price" not in data or not data['disc_price']:
            return Response({"Error": "disc_price not Found"})
        if "status" not in data or not data['status']:
            return Response({"Error": "status not Found"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "product" not in data or not data['product']:
            return Response({"Error": "product not Found"})
        if "xaraktristika" not in data or not data['xaraktristika']:
            return Response({"Error": "xaraktristika not Found"})
        if "opesaniya" not in data or not data['opesaniya']:
            return Response({"Error": "opesaniya not Found"})
        if "vapros" not in data or not data['vapros']:
            return Response({"Error": "vapros not Found"})
        if "img" not in data or not data['img']:
            return Response({"Error": "product not Found"})
        if "title" not in data or not data['title']:
            return Response({"Error": "title not Found"})
        if "shop_name" not in data or not data['shop_name']:
            return Response({"Error": "shop_name not Found"})
        if "desc" not in data or not data['desc']:
            return Response({"Error": "desc not Found"})
        if "color" not in data or not data['color']:
            return Response({"Error": "color not Found"})
        if "quent" not in data or not data['quent']:
            return Response({"Error": "quent not Found"})
        if "price" not in data or not data['price']:
            return Response({"Error": "price not Found"})
        if "disc_price" not in data or not data['disc_price']:
            return Response({"Error": "disc_price not Found"})
        if "status" not in data or not data['status']:
            return Response({"Error": "status not Found"})

        prod = Product.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=prod)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        prod = Product.objects.filter(id=pk).first()
        if not prod:
            return Response({'Error': 'Product not Found'})
        prod.delete()
        return Response({"Success": "Product Deleted"})

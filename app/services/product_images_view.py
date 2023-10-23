from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.models.core import Product_images
from app.serializers import ProductImageSerializer


class ProductImagesView(GenericAPIView):
    serializer_class = ProductImageSerializer

    def get(self, request, pk=None):
        if pk:
            ctg = Product_images.objects.filter(id=pk).first()
            if ctg:
                ser = self.get_serializer(ctg).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        imgs = Product_images.objects.all()
        ser = self.get_serializer(imgs, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "img" not in data or not data['img']:
            return Response({"Error": "Not Found"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "img" not in data or not data['img']:
            return Response({"Error": "Not Found"})

        ctg = Product_images.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=ctg)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        ctg = Product_images.objects.filter(id=pk).first()
        if not ctg:
            return Response({'Error': 'Not Found'})
        ctg.delete()
        return Response({"Success": "Img Deleted"})

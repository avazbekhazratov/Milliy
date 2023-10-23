from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.models import Xarakteristika
from app.serializers import XarakteristikaSerializers


class ProductView(GenericAPIView):
    serializer_class = XarakteristikaSerializers

    def get(self, request, pk=None):
        if pk:
            xarak = Xarakteristika.objects.filter(id=pk).first()
            if xarak:
                ser = self.get_serializer(xarak).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        xarakt = Xarakteristika.objects.all()
        ser = self.get_serializer(xarakt, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        required_keys = [
            "protssesor", "ram", "kesh", "chipset", "screen",
            "ekran", "tip", "matritsa", "chastota",
            "video_karta", "video_prot", "video_tip"
        ]

        for key in required_keys:
            if key not in data or not data[key]:
                return Response({"Error": "Not Found"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        required_keys = [
            "protssesor", "ram", "kesh", "chipset", "screen",
            "ekran", "tip", "matritsa", "chastota",
            "video_karta", "video_prot", "video_tip"
        ]

        for key in required_keys:
            if key not in data or not data[key]:
                return Response({"Error": "Not Found"})

        prod = Xarakteristika.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=prod, partial=True)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        prod = Xarakteristika.objects.filter(id=pk).first()
        if not prod:
            return Response({'Error': 'Not Found'})
        prod.delete()
        return Response({"Success": "Product Deleted"})

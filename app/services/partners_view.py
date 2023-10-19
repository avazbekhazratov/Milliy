from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from app.serializers import PartnersSerializers
from app.models.core import Partners


class PartnersView(GenericAPIView):
    serializer_class = PartnersSerializers

    def get(self, request, pk=None):
        if pk:
            partner = Partners.objects.filter(id=pk).first()
            if partner:
                ser = self.get_serializer(partner).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        partners = Partners.objects.all()
        ser = self.get_serializer(partners, many=True).data
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

        partner = Partners.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=partner)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        partner = Partners.objects.filter(id=pk).first()
        if not partner:
            return Response({'Error': 'Not Found'})
        partner.delete()
        return Response({"Success": "Category Deleted"})

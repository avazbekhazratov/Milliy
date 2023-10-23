from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import Opesaniyaserializer
from app.models.core import Opesaniya


class CategoryView(GenericAPIView):
    serializer_class = Opesaniyaserializer

    def get(self, request, pk=None):
        if pk:
            opisanya = Opesaniya.objects.filter(id=pk).first()
            if opisanya:
                ser = self.get_serializer(opisanya).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found Opisaniya"})
        opisanyas = Opesaniya.objects.all()
        ser = self.get_serializer(opisanyas, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "img" not in data or not data['img']:
            return Response({"Error": "Not Found Imaga"})
        if "title" not in data or not data['title']:
            return Response({"Error": "Not Found Title"})
        if "text" not in data or not data['text']:
            return Response({"Error": "Not Found Text"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "img" not in data or not data['img']:
            return Response({"Error": "Not Found Image"})

        if "title" not in data or not data['title']:
            return Response({"Error": "Not Found Title"})

        if "text" not in data or not data['text']:
            return Response({"Error": "Not Found Text"})

        opisanya = Opesaniya.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=opisanya)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        opisanya = Opesaniya.objects.filter(id=pk).first()
        if not opisanya:
            return Response({'Error': 'Opisanya Not Found'})
        opisanya.delete()
        return Response({"Success": "Opisanya Deleted"})

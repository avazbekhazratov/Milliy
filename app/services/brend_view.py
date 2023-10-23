from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import BrendSerializers
from app.models import Brend


class MainView(GenericAPIView):
    serializer_class = BrendSerializers

    def get(self, request, pk=None):
        if pk:
            brend = Brend.objects.filter(id=pk).first()
            if brend:
                ser = self.get_serializer(brend).data
                return Response({'Success': ser})
            return Response({'Error': "Brend not Found"})
        brends = Brend.objects.all()
        ser = self.get_serializer(brends, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "title" not in data or not data['title']:
            return Response({"Error": "title not Found "})

        if "img" not in data or not data['img']:
            return Response({"Error": "img not Found"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "title" not in data or not data['title']:
            return Response({"Error": "title not Found "})

        if "img" not in data or not data['img']:
            return Response({"Error": "img not Found"})

        brends = Brend.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=brends)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        brend = Brend.objects.filter(id=pk).first()
        if not brend:
            return Response({'Error': 'brend not Found'})
        brend.delete()
        return Response({"Success": "Brend Deleted"})



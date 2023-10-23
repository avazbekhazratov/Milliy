from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import MainSerializers
from app.models import Main


class MainView(GenericAPIView):
    serializer_class = MainSerializers

    def get(self, request, pk=None):
        if pk:
            main = Main.objects.filter(id=pk).first()
            if main:
                ser = self.get_serializer(main).data
                return Response({'Success': ser})
            return Response({'Error': "Main Found"})
        mains = Main.objects.all()
        ser = self.get_serializer(mains, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "img" not in data or not data['img']:
            return Response({"Error": " img not Found"})
        if "title" not in data or not data['title']:
            return Response({"Error": " title not Found"})
        if "title_desc" not in data or not data['title_desc']:
            return Response({"Error": " title_desc not Found"})
        if "title_com" not in data or not data['title_com']:
            return Response({"Error": " title_com not Found"})
        if "title_com_desc" not in data or not data['title_com_desc']:
            return Response({"Error": " title_com_desc not Found"})
        if "title_ass" not in data or not data['title_ass']:
            return Response({"Error": " title_ass not Found"})
        if "title_ass_desc" not in data or not data['title_ass_desc']:
            return Response({"Error": " title_ass_desc not Found"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data

        if "img" not in data or not data['img']:
            return Response({"Error": " img not Found"})
        if "title" not in data or not data['title']:
            return Response({"Error": " title not Found"})
        if "title_desc" not in data or not data['title_desc']:
            return Response({"Error": " title_desc not Found"})
        if "title_com" not in data or not data['title_com']:
            return Response({"Error": " title_com not Found"})
        if "title_com_desc" not in data or not data['title_com_desc']:
            return Response({"Error": " title_com_desc not Found"})
        if "title_ass" not in data or not data['title_ass']:
            return Response({"Error": " title_ass not Found"})
        if "title_ass_desc" not in data or not data['title_ass_desc']:
            return Response({"Error": " title_ass_desc not Found"})

        main = Main.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=main)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        main = Main.objects.filter(id=pk).first()
        if not main:
            return Response({'Error': 'Main not Found'})
        main.delete()
        return Response({"Success": "Main Deleted"})



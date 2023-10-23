from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import Xaridordan_Ser
from app.models import News_add


class New_add_View(GenericAPIView):
    serializer_class = News_add_Ser

    def get(self, request, pk=None):
        if pk:
            main = News_add.objects.filter(id=pk).first()
            if main:
                ser = self.get_serializer(main).data
                return Response({'Success': ser})
            return Response({'Error': "main not Found"})
        mains = News_add.objects.all()
        ser = self.get_serializer(mains, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "title" not in data or not data['title']:
            return Response({"Error": "Data to`liq emas "})
        if "img" not in data or not data['img']:
            return Response({"Error": "Data to`liq emas"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "title" not in data or not data['title']:
            return Response({"Error": "Not Found"})
        if "img" not in data or not data['img']:
            return Response({"Error": "Data to`liq emas"})
        main = News_add.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=main)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        main = News_add.objects.filter(id=pk).first()
        if not main:
            return Response({'Error': 'Not Found'})
        main.delete()
        return Response({"Success": "Category Deleted"})



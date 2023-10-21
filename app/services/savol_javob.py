from app.models import Savol_Javoblar
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from app.serializers import Savol_Serializer


class Savol_View(GenericAPIView):
    serializer_class = Savol_Serializer

    def get(self, request):
        savol = Savol_Javoblar.objects.all()
        ser = self.get_serializer(savol, many=True).data
        return Response({'Savollar': ser})

    def post(self, request):
        data = request.data
        if "text" not in data or not data['text']:
            return Response({"Error": "Savol qani"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    # def put(self, request, pk):
    #     data = request.data
    #     if "text" not in data or not data['text']:
    #         return Response({"Error": "Not Found"})
    #
    #     savol = Savol_Javoblar.objects.filter(pk=pk).first()
    #     ser = self.get_serializer(data=data, instance=savol)
    #     if ser.is_valid(raise_exception=True):
    #         ser.save()
    #         return Response({"Success": ser.data})

    def delete(self, request, pk):
        savol = Savol_Javoblar.objects.filter(id=pk).first()
        if not savol:
            return Response({'Error': 'Savol yoq'})
        savol.delete()
        return Response({"Success": "Savol Deleted"})

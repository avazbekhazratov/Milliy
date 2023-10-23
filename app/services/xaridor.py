from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import Xaridordan_Ser
from app.models import Xaridordan_savol


class XaridorView(GenericAPIView):
    serializer_class = Xaridordan_Ser

    def get(self, request, pk=None):
        if pk:
            main = Xaridordan_savol.objects.filter(id=pk).first()
            if main:
                ser = self.get_serializer(main).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        mains = Xaridordan_savol.objects.all()
        ser = self.get_serializer(mains, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "savol_turi" not in data or not data['savol_turi']:
            return Response({"Error": "Data to`liq emas "})
        if "javobi" not in data or not data['javobi']:
            return Response({"Error": "Data to`liq emas"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "savol_turi" not in data or not data['savol_turi']:
            return Response({"Error": "Not Found"})
        if "javobi" not in data or not data['javobi']:
            return Response({"Error": "Data to`liq emas"})
        main = Xaridordan_savol.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=main)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        main = Xaridordan_savol.objects.filter(id=pk).first()
        if not main:
            return Response({'Error': 'Not Found'})
        main.delete()
        return Response({"Success": "Category Deleted"})



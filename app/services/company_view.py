from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import CompanySerializers
from app.models import Company


class MainView(GenericAPIView):
    serializer_class = CompanySerializers

    def get(self, request, pk=None):
        if pk:
            company = Company.objects.filter(id=pk).first()
            if company:
                ser = self.get_serializer(company).data
                return Response({'Success': ser})
            return Response({'Error': "Company not Found"})
        companies = Company.objects.all()
        ser = self.get_serializer(companies, many=True).data
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

        companies = Company.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=companies)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        company = Company.objects.filter(id=pk).first()
        if not company:
            return Response({'Error': 'Company not Found'})
        company.delete()
        return Response({"Success": "Company Deleted"})



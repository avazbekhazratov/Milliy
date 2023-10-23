from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import ContactSerializers
from app.models import Contact


class MainView(GenericAPIView):
    serializer_class = ContactSerializers

    def get(self, request, pk=None):
        if pk:
            cantact = Contact.objects.filter(id=pk).first()
            if cantact:
                ser = self.get_serializer(cantact).data
                return Response({'Success': ser})
            return Response({'Error': "Contact not Found"})
        cantacts = Contact.objects.all()
        ser = self.get_serializer(cantacts, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "phone" not in data or not data['phone']:
            return Response({"Error": "phone not Found "})

        if "email" not in data or not data['email']:
            return Response({"Error": "phone not Found"})

        if "location" not in data or not data['location']:
            return Response({"Error": "phone not Found"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "phone" not in data or not data['phone']:
            return Response({"Error": "phone not Found "})

        if "email" not in data or not data['email']:
            return Response({"Error": "phone not Found"})

        if "location" not in data or not data['location']:
            return Response({"Error": "phone not Found"})

        contact = Contact.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=contact)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        contact = Contact.objects.filter(id=pk).first()
        if not contact:
            return Response({'Error': 'Contact not Found'})
        contact.delete()
        return Response({"Success": "Contact Deleted"})



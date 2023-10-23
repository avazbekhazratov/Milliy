from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import Partners_logo_Serializers, AdvertSerializers, NewsSerializers
from app.models import Partners_logo, Advert, News


class Partnres_logo_View(GenericAPIView):
    serializer_class = Partners_logo_Serializers

    def get(self, request, pk=None):
        if pk:
            part = Partners_logo.objects.filter(id=pk).first()
            if part:
                ser = self.get_serializer(part).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        partnres_logo = Partners_logo.objects.all()
        ser = self.get_serializer(partnres_logo, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "img" not in data or not data['img']:
            return Response({"Error": "Not Found img"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "img" not in data or not data['img']:
            return Response({"Error": "Not Found img"})

        partners_logo = Partners_logo.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=partners_logo)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        logo = Partners_logo.objects.filter(id=pk).first()
        if not logo:
            return Response({'Error': 'Not Found !'})
        logo.delete()
        return Response({"Success": "Partners_logo Deleted"})


class AdverntView(GenericAPIView):
    serializer_class = AdvertSerializers

    def get(self, request, pk=None):
        if pk:
            part = Advert.objects.filter(id=pk).first()
            if part:
                ser = self.get_serializer(part).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        advert = Partners_logo.objects.all()
        ser = self.get_serializer(advert, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "logo" not in data or not data['logo']:
            return Response({"Error": "Not Found logo"})

        if "title" not in data or not data['title']:
            return Response({"Error": "Not Found title"})

        if "info" not in data or not data['info']:
            return Response({"Error": "Not Found info"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "logo" not in data or not data['logo']:
            return Response({"Error": "Not Found logo"})

        if "title" not in data or not data['title']:
            return Response({"Error": "Not Found title"})

        if "info" not in data or not data['info']:
            return Response({"Error": "Not Found info"})

        advert = Advert.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=advert)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        advert = Advert.objects.filter(id=pk).first()
        if not advert:
            return Response({'Error': 'Not Found !'})
        advert.delete()
        return Response({"Success": "Advert Deleted"})


class NewsView(GenericAPIView):
    serializer_class = NewsSerializers

    def get(self, request, pk=None):
        if pk:
            news = News.objects.filter(id=pk).first()
            if news:
                ser = self.get_serializer(news).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found"})
        new = News.objects.all()
        ser = self.get_serializer(new, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data

        if "title" not in data or not data['title']:
            return Response({"Error": "Not Found title"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "title" not in data or not data['title']:
            return Response({"Error": "Not Found title"})

        news = News.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=news)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        news = News.objects.filter(id=pk).first()
        if not news:
            return Response({'Error': 'Not Found !'})
        news.delete()
        return Response({"Success": "News Deleted"})

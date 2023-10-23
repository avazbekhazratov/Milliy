from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app.serializers import Feed_backserializer
from app.models.core import FeedBack



class FeedbackView(GenericAPIView):
    serializer_class = Feed_backserializer

    def get(self, request, pk=None):
        if pk:
            feed_back = FeedBack.objects.filter(id=pk).first()
            if feed_back:
                ser = self.get_serializer(feed_back).data
                return Response({'Success': ser})
            return Response({'Error': "Not Found feed_back"})
        feed_backs = FeedBack.objects.all()
        ser = self.get_serializer(feed_backs, many=True).data
        return Response({'Success': ser})

    def post(self, request):
        data = request.data
        if "user" not in data or not data['user']:
            return Response({"Error": "Not Found User"})
        if "reating" not in data or not data['reating']:
            return Response({"Error": "Not Found Reating"})
        if "text" not in data or not data['text']:
            return Response({"Error": "Not Found Text"})

        ser = self.get_serializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def put(self, request, pk):
        data = request.data
        if "user" not in data or not data['user']:
            return Response({"Error": "Not Found User"})

        if "reating" not in data or not data['reating']:
            return Response({"Error": "Not Found Reating"})

        if "text" not in data or not data['text']:
            return Response({"Error": "Not Found Text"})

        feed = FeedBack.objects.filter(pk=pk).first()
        ser = self.get_serializer(data=data, instance=feed)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"Success": ser.data})

    def delete(self, request, pk):
        feed = FeedBack.objects.filter(id=pk).first()
        if not feed:
            return Response({'Error': 'FeedBack Not Found'})
        feed.delete()
        return Response({"Success": "FeedBack Deleted"})

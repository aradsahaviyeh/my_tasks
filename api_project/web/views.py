from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer

from .models import Message


# This class is for receiving view and post data
class MessageView(APIView):

    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
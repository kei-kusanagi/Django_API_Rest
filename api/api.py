from django.urls import is_valid_path
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status


class UserAPI(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        serializer = UserSerializer(data = request.data)
        user = serializer.delete()
        return Response(serializer.data, status = status.HTTP_200_OK)
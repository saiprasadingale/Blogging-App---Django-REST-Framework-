from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response

@api_view(http_method_names=['POST'])
def user_api(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=201)
    return Response(data=serializer.errors, status=400)
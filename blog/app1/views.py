from rest_framework import status
from .models import *
from .serializers import BlogSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(http_method_names=['GET', "POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def blog_api(request):
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        blogs = Blogs.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def blog_details_api(request, pk=None):
    blog = get_object_or_404(Blogs, pk=pk)
    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        serializer = BlogSerializer(data=request.data, instance=blog)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        blog.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PATCH':
        serializer = BlogSerializer(data=request.data, instance=blog, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
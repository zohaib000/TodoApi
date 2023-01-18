from os import stat
from django.contrib.auth.models import User
from pkgutil import get_data
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.views import View
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.
class todos(APIView):
    def get(self,request):
        user=request.GET.get('user')
        todos=Todo.objects.filter(User=user)
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class todo(APIView):
    def get_data(self,pk):
        return Todo.objects.get(id=pk)
    
    def get(self,rquest,pk):
        serializer=TodoSerializer(self.get_data(pk))
        return Response(serializer.data)
        
    def put(self,request,pk):
        seria=TodoSerializer(self.get_data(pk),data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data)
        return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        data=self.get_data(pk)
        data.delete()
        return Response('Post Deleted',status=status.HTTP_204_NO_CONTENT)
    


        

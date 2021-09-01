from decimal import Context
from django.http.response import Http404
from requests.api import delete
from requests.sessions import Request
from rest_framework import serializers, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from article.models import textData
from article.api.serializers import textSerializer
import requests
import os


class apiView(APIView):
    def get (self,request,pk=None,format=None):
        
        # import ipdb;ipdb.set_trace() 

        if  pk == None:
            texts = textData.objects.all()
            serializer = textSerializer(texts,many=True)
            
            return Response(serializer.data)
            
        else:
           texts=textData.objects.get(pk)
           serializer = textSerializer(texts,many=False)
           return Response(serializer.data)

    def post(self,request,pk=None,format=None):
        if  pk == None:
            texts = textData.objects.all()
            serializer = textSerializer(texts,many=True)

            #create 
            serializer =  textSerializer(data=request.data)
            if serializer.is_valid():      # == True 
                serializer.save()          # serilazer veritabanına kayıt edildi 
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)
           
            
        else:
           texts=textData.objects.get(pk)
           serializer =  textSerializer(texts,data=request.data)
           
            #update
           if serializer.is_valid():      # == True 
                serializer.save()          # serilazer veritabanına kayıt edildi 
                return Response(serializer.data)
           return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
         if pk == None:
            texts = textData.objects.all()
            serializer = textSerializer(texts,many=True)
            return Response(serializer.data)
            
         else:
           texts=textData.objects.get(pk)
           serializer = textSerializer(texts,many=False)
           texts.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)


class apiViewRequest(APIView):
    def get(self,request,pk,format=None):

        response = os.environ.get('REQUEST_URL')

        predict_request=requests.post(response+'/train/')

        return Response(predict_request.json())
    
    def post(self,request,pk,format=None):
        serializer =  textSerializer(data=request.data , context={'request':request})
        if serializer.is_valid(raise_exception=True):      # == True 
            serializer.save()          # serilazer veritabanına kayıt edildi 
            response = os.environ.get('REQUEST_URL')

            predict_request=requests.post(response+'/predict/')

            return Response(predict_request.json())

            # return Response(serializer.data, status=status.HTTP_201_CREATED) # veri başarılı şekilde kayıt edildi mesajı
        return Response(status=status.HTTP_400_BAD_REQUEST)

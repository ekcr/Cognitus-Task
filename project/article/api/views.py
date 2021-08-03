from decimal import Context
from rest_framework import serializers, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from article.models import textData
from article.api.serializers import textSerializer
import requests

@api_view(['GET','POST'])

def text_list_create_api_view(request):
    
    # import ipdb;ipdb.set_trace() 
    if request.method == 'GET':
        texts = textData.objects.all()
        serializer = textSerializer(texts,many=True)

        response = requests.get('http://127.0.0.1:8000/train')
        if response.status_code == 200:
            return Response( response.json())
        elif response.status_code == 404:
            print('Not Found.')


    elif request.method == 'POST':      #gönderilen istek post olusturma ise..
        serializer =  textSerializer(data=request.data , context={'request':request})
        if serializer.is_valid(raise_exception=True):      # == True 
            serializer.save()          # serilazer veritabanına kayıt edildi 
            return Response(serializer.data, status=status.HTTP_201_CREATED) # veri başarılı şekilde kayıt edildi mesajı
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])

def text_detail(request,pk):

    try:
        texts= textData.objects.get(pk=pk)
    
    except textData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = textSerializer(texts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer =  textSerializer(texts,data=request.data)
        if serializer.is_valid():      # == True 
            serializer.save()          # serilazer veritabanına kayıt edildi 
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        texts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
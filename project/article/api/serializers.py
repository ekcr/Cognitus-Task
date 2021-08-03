from typing import Text
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from article.models import textData

class textSerializer(serializers.ModelSerializer):
    # import ipdb;ipdb.set_trace() 
    class Meta:
        model = textData
        fields = ['text', 'label']


# class textSerializer(serializers.Serializer):
#     text = serializers.CharField()
#     label = serializers.CharField()

#     def save(self, **kwargs):

#         data = self.validated_data
#         text = data['text']
#         label = data['label']


#         textData.objects.create(text=text, label=label)



        


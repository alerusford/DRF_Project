from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Women

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'

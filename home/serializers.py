from attr import fields
from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


        
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields="__all__"
    
# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *  

class MenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu
        fields = '__all__'  # This will include all fields of the Menu model
        # Alternatively, you can specify the fields explicitly
        # fields = ['field1', 'field2', 'field3']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['_all_']        


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']
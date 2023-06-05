from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    charity_name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)
    about = serializers.CharField(max_length=200)
    charity_abn = serializers.IntegerField()
    

    def create(self,validated_data):
        return CustomUser.objects.create(**validated_data)
from accounts.models import Register,History
from rest_framework import serializers
# from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Register
        fields = ["Name",'id',"email","date_birth","userRole","address","password"]
        
        
class Historyserializer(serializers.ModelSerializer):
            
            class Meta:
                  model =History
                  fields="__all__"                              
            
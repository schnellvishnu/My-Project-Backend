from sapdb.models import SapProducts
from rest_framework import serializers

class ProductdbSerializer(serializers.ModelSerializer):
     class Meta:
       model=SapProducts
       fields= "__all__"
                    
                                        
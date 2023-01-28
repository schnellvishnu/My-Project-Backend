from masterapp.models import Company,Customers, Stock,Products,Shipping
from rest_framework import serializers
class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Company
        fields="__all__"
        # fields=["id","name","zip","state","country","created_at"]
class CustomersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Customers
        # fields="__all__"
        fields=["id","name","address","state","country","created_by","city","description","company_name"]

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields=["id","ponumber","name","description",
                "created_by",
                "created_at",'updated_at',
                "status"
                ]
        
class ProductPropertySerializer(serializers.ModelSerializer):
               class Meta:
                    model = Products
                    fields=["id","batch_number","manufacturing_date","exp_date",
                    "License_Number"
                    
                    ]                 
class ShipPOSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shipping
        # fields="__all__"
        fields = ["id","shipping_order_name","ponumber","company","date","createdby","status","po"]
        
        
        
class StockSerializer(serializers.ModelSerializer):
      
      class Meta:
        model =Stock
        fields="__all__"
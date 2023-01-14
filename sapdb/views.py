from django.shortcuts import render
from .models import SapProducts
from .serializers import ProductdbSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics


# Create your views here.
class Productdbview(APIView):
      def get(self,request):
              detailobj=SapProducts.objects.all()
              serializerobj=ProductdbSerializer(detailobj,many=True)
              return Response(serializerobj.data) 

class Productdbindividualview(APIView):
              def get(self,request,id):
                      detailobj=SapProducts.objects.all().filter(ponumber=id)
                      serializerobj=ProductdbSerializer(detailobj,many=True)
                      return Response(serializerobj.data)                                           


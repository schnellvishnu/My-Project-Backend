from django.shortcuts import render
from rest_framework import generics

from masterapp.models import Company, Customers,Stock,Products,Shipping
from accounts.models import History
from masterapp.serializers import CompanySerializer, CustomersSerializer,StockSerializer,ShipPOSerializer,ProductSerializer
# from masterapp.permissions import ObjectDestroyPermission, Productpermission
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from masterapp import serializers
import datetime
# from django_filters.rest_framework import  DjangoFilterBackend
# from apps_extra_code.custom_list_search_filter import CustomSearchFilter



class CompanyView(APIView):
    def get(self, request):
        detailsObj = Company.objects.all()
        serializeObj = CompanySerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = CompanySerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelname="Company",
                                savedid=device.id,
                                operationdone="create",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
            return Response(request.data['loggedInUser'])
        return Response(serializeObj.errors)

class updateCompany(APIView):
    def put(self, request, pk):
        try:
            detailObj = Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = CompanySerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History(modelname="Company",
                                savedid=pk,
                                operationdone="update",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteCompany(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        historysave=History(modelname="Company",
                                savedid=pk,
                                operationdone="delete",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
        historysave.save()
        return Response(200)
class  Companyindividual(APIView):
    def get(self, request, id):
        detailsObj =Company.objects.all().filter(id=id)
        serializeObj = CompanySerializer(detailsObj, many=True)
        return Response(serializeObj.data)     
 #/////////////////////////////////////////////////////////////////////////////     
      
class ProductView(APIView):

                        
    def get(self, request):
        detailsObj =Products.objects.all()
        serializeObj = ProductSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj =ProductSerializer(data=request.data)
        if serializeObj.is_valid():
            device= serializeObj.save()
            historysave=History(modelname="Products",
                                savedid=device.id,
                                operationdone="create",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
           
            
            return Response(200)
        return Response(serializeObj.errors)

class updateProduct(APIView):
    def put(self, request, pk):
        try:
            detailObj =Products.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ProductSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            
            if request.data['status']=='Closed':
                stocksave=Stock(ponumber=request.data["ponumber"],
                                       name=request.data['name'],
                                       description=request.data['description'],
                                       created_by=request.data['created_by'],
                                       created_at=request.data['created_at'],
                                       updated_at=request.data['updated_at'],
                                       status=request.data['status'])
                stocksave.save()                        
                                    
            
            historysave=History(modelname="Products",
                                savedid=pk,
                                operationdone="update",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
           
            
            return Response(200)
        return Response(serializeObj.errors)

class deleteProduct(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Products.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        historysave=History(modelname="Products",
                                savedid=pk,
                                operationdone="delete",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
        historysave.save()
           
        return Response(200)

class  Productindividual(APIView):
    def get(self, request, id):
        detailsObj =Products.objects.all().filter(id=id)
        serializeObj = ProductSerializer(detailsObj, many=True)
        return Response(serializeObj.data)       

#/////////////////////////////////////////////////////////////////////////////////

class ShipPOView(APIView):
    def get(self, request):
        detailsObj =Shipping.objects.all()
        serializeObj = ShipPOSerializer(detailsObj, many = True)
        return Response(serializeObj.data)
    

   
    def post(self, request):
        serializeObj =ShipPOSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            
            
            record = Products.objects.get(id=request.data["ponumber"])
            record.status = "Shipping"
            record.save()
            if request.method == 'POST': 
                ponumber=request.data['po'] 
                stockObj = Stock.objects.all().filter(ponumber=ponumber)
                stockObj.delete()
            historysave=History(modelname="Shipping",
                                savedid=device.id,
                                operationdone="create",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class updateShipPO(APIView):
    def put(self, request, pk):
        try:
            detailObj =Shipping.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ShipPOSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History(modelname="Shipping",
                                savedid=pk,
                                operationdone="update",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteShipPO(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Shipping.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        historysave=History(modelname="Shipping",
                                savedid=pk,
                                operationdone="delete",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
        historysave.save()
        return Response(200)
class ShippoViewIndividual(APIView):
      def get(self, request, id):
        detailsObj = Shipping.objects.all().filter(id=id)
        serializeObj = ShipPOSerializer(detailsObj, many=True)
        return Response(serializeObj.data)
      
      
  #/////////////////////////////////////////////////////////////////////////////    
      
class CustomersView(APIView):
    def get(self, request):
        detailsObj = Customers.objects.all()
        serializeObj = CustomersSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = CustomersSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelname="Customers",
                                savedid=device.id,
                                operationdone="create",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateCustomer(APIView):
    def put(self, request, pk):
        try:
            detailObj =Customers.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = CustomersSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History(modelname="Customers",
                                savedid=pk,
                                operationdone="update",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteCustomer(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Customers.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        historysave=History(modelname="Customers",
                                savedid=pk,
                                operationdone="delete",
                                donebyuser=request.data['loggedInUser'],
                                donebyUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
        historysave.save()
        return Response(200)
    
class CustomerViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = Customers.objects.all().filter(id=id)
        serializeObj = CustomersSerializer(detailsObj, many=True)
        return Response(serializeObj.data)       
      
      
 #///////////////////////////////////////////////////////////////////////////////////     
      
class StockView(APIView):
    def get(self, request):
        detailsObj =Stock.objects.all()
        serializeObj = StockSerializer(detailsObj, many = True)
        return Response(serializeObj.data)
  
   


  
    def post(self, request):
        serializeObj =StockSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateStock(APIView):
    def put(self,request,pk):
        try:
            detailObj =Stock.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = StockSerializer(detailObj,data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteStock(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Stock.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)

class Stockclosedview(APIView):
       def get(self, request):
            detailsObj = Products.objects.all().filter(status='Closed')
            serializeObj = ProductSerializer(detailsObj, many=True)
            return Response(serializeObj.data)                
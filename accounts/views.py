from accounts.models import  Register,History
from accounts.serializers import RegisterSerializer,Historyserializer
# from masterapp.permissions import ObjectDestroyPermission, Productpermission
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts import serializers
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User


class RegisterView(APIView):
  
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        detailsObj = Register.objects.all()
        serializeObj =RegisterSerializer(detailsObj, many = True)
        return Response(serializeObj.data)


    def post(self, request):
            serializeObj = RegisterSerializer(data=request.data)
            if serializeObj.is_valid():
                serializeObj.save()

                # ##########  Registering the user in User model
                userMail = request.data['email']
                userName = request.data['Name']
                userPassword =request.data ['password']
                user = User.objects.create_user(username=userMail, email=userMail, password=userPassword)
                user.save()

                return Response(200)
            return Response(serializeObj.errors)  

    # def post(self, request):
    #     serializeObj = RegisterSerializer(data=request.data)
    #     if serializeObj.is_valid():
    #         serializeObj.save()
    #         return Response(200)
    #     return Response(serializeObj.errors)



	    

class updateRegister(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        try:
            detailObj = Register.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = RegisterSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class deleteRegister(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            detailsObj = Register.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)

class userAuthVerify(APIView):
                    
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def post(self, request):
		userData = Register.objects.filter(email=request.data['username']).values()
		return Response(userData[0]['userRole'])
# class logInController(APIView):
#     def post(self,request):
#         userData=Register.objects.filter(email=request.data['username']).values()
#         if(userData):
#             if(userData[0]['password']==request.data['password']):
#                 return Response(userData[0]['userRole'])
#             else:
#                 return Response("passwordDoesNotMatch") 
#         else:
#             return Response("UserDoesNotExit")                       
        
                                
     

  

	# def post(self, request):
	# 	return Response(201)

#________________________________________________________
class HistoryView(APIView):
    def get(self,request):
        detailsObj = History.objects.all()
        serializeObj = Historyserializer(detailsObj, many =True)
        return Response(serializeObj.data)
    
class deleteHistory(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = History.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)    
    

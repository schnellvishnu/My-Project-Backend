from django.db import models

# Create your models here.

batch_status =(('Draft','Draft'), 
         ('Shipping','Shipping'),  ('Closed','Closed'), ('Fullyreleased','Fullyreleased'),)
# Create your models here.
class Products(models.Model):
  id = models.AutoField(primary_key=True)
  ponumber=models.CharField(max_length=100, unique=True)
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(max_length =100,null=True,blank=True)
  created_by = models.CharField(max_length =100)
  created_at = models.DateTimeField(auto_now_add=False,null=True)
  updated_at = models.DateTimeField(auto_now_add=False,null=True)
  status = models.CharField(max_length=20, default='Draft')
  
  batch_number=models.IntegerField(max_length=100,null=True)
  manufacturing_date=models.DateField(null=True)
  exp_date=models.DateField(null=True)
  License_Number=models.IntegerField(max_length=100,null=True)
  
  
  def __str__(self):
        return self. ponumber
      
      
      
class Company(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=100,unique=True)
  zip = models.CharField(max_length=20)
  state = models.CharField(max_length=20)
  country = models.CharField(max_length=20)
  created_at = models.DateField(null=True)
  def __str__(self):
    return self.name 
  
class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    created_by = models.CharField(max_length =100)
    description = models.TextField(max_length =100)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    company_name= models.ForeignKey(Company,related_name='company_to_customers',on_delete=models.CASCADE) 
    def __str__(self):
      return self.name 

class Shipping(models.Model):
  id = models.AutoField(primary_key=True)
  shipping_order_name = models.CharField(max_length=40)
  ponumber=models.ForeignKey(Products,related_name='products_to_shipping',on_delete=models.CASCADE,default=False)
  company=models.ForeignKey(Company,on_delete=models.CASCADE)
  date=models.DateField(null=True)
  createdby=models.CharField(max_length=100)
  status=models.CharField(max_length=100,default='Shipping')
  po=models.CharField(max_length=40,null=True)
  def __str__(self):
      return self.shipping_order_name 
  
  
  
class Stock(models.Model):
  id = models.AutoField(primary_key=True)
  ponumber=models.IntegerField(max_length=100, unique=True)
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(blank= True, null= True)
  created_by = models.CharField(max_length =100)
  created_at = models.DateTimeField(auto_now_add=False,null=True)
  updated_at = models.DateTimeField(auto_now=False,null=True)
  status = models.CharField(max_length=20, choices = batch_status,default='Draft')
  def __str__(self):
        return self.name 
 
 
      
     
          
      
  
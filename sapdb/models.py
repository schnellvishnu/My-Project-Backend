from django.db import models

# Create your models here.

batch_status =(('Draft','Draft'), 
         ('Shipping','Shipping'),  ('Closed','Closed'), ('Fullyreleased','Fullyreleased'),)
# Create your models here.
class SapProducts(models.Model):
  id = models.AutoField(primary_key=True)
  ponumber=models.CharField(max_length=100, unique=True)
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(max_length =100,null=True,blank=True)
  created_by = models.CharField(max_length =100)
  created_at = models.DateTimeField(auto_now_add=False,null=True)
  updated_at = models.DateTimeField(auto_now_add=False,null=True)
  status = models.CharField(max_length=20, choices = batch_status,default='Draft')
  def __str__(self):
        return self. ponumber
      
      
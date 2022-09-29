from turtle import position
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Province(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=30)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Barangay(models.Model):
    name = models.CharField(max_length=30)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    def __str__(self):
        return self.name   

class Emp(models.Model):
  business_name = models.CharField(max_length=200, null=True)
  registered_name = models.CharField(max_length=200, null=True)
  tin = models.CharField(max_length=15,null=True)
  building =  models.CharField(max_length=40, null=True)
  barangay =  models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True)
  municipality =  models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True)
  province =  models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
  zip_code =  models.CharField(max_length=10)
  telephone =  models.IntegerField(null=False)
  fax_number =  models.IntegerField(blank=True,null=True)
  email = models.EmailField(unique=True, null=True)
  manager = models.CharField(max_length=50, null=True)
  main_economic_activity = models.CharField(max_length=200, null=True)
  major_products = models.CharField(max_length=200, blank= True)
  legal_organization = models.CharField(max_length=50, null=True)
  economic_organization = models.CharField(max_length=50, null=True)
  total_employment =  models.IntegerField()
  male =  models.IntegerField(null=True)
  female =  models.IntegerField(null=True)
  alien =  models.IntegerField(blank=True,null=True)
  regular =  models.IntegerField(null=True)
  non_regular =  models.IntegerField(null=True)
  below_15 =  models.IntegerField(blank=True,null=True)  
  above_15 =  models.IntegerField(blank=True,null=True)
  labor_union = models.CharField(max_length=200,blank=True,null=True)
  total_number_of_subcontactors = models.IntegerField(blank=True,null=True)
  total_number_of_subcontracted_employees = models.IntegerField(blank=True,null=True)
  representative_name = models.CharField(max_length=200, null=True)
  position =  models.CharField(max_length=40, null=True)
  telephone_number =  models.IntegerField(null=True)
  fax_number =  models.IntegerField(blank=True,null=True)
  email_add = models.EmailField(unique=True, null=True)

  def __str__(self):
    return self.tin

class User_office(models.Model):
  user_name= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  office = models.CharField(max_length=200, null=True)
  province = models.ForeignKey(Province, on_delete=models.CASCADE)
  address = models.CharField(max_length=200, null=True)
  head = models.CharField(max_length=200, null=True)
  position = models.CharField(max_length=200, null=True)

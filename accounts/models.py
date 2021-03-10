from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from datetime import date


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_financer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField(default='abc@xyz.com',max_length=50)
    phone_number = models.CharField(default='8469211691',max_length=10)
  

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name

class Financer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    CompanyName = models.CharField(max_length=50,default='abc')
    interest_rate = models.CharField(max_length=100)
    
    Address = models.CharField(max_length=200,default='Enter Address Here')
    City = models.CharField(max_length=100)
    logo=models.ImageField(upload_to='images/',null=True,blank=True)

    def get_absolute_url(self):
        return reverse('findetails', args=[str(self.user_id)])


    def __str__(self):
        return self.user.first_name



class sellcar(models.Model):
  

    Ownername=models.CharField(default=None,max_length=250)
    Contactnumber=models.CharField(default=None,max_length=10)
    Email=models.EmailField(default=None,max_length=50)
    brand=models.CharField(default=None,max_length=250)
    modelname=models.CharField(default=None,max_length=250)
    yearofmanufacture=models.CharField(default=None,max_length=4)
    kilometersdone=models.CharField(default=None,max_length=6)
    fueltype=models.CharField(default=None,max_length=10)
    noofowners=models.CharField(default=None,max_length=2)
    price=models.CharField(default=None,max_length=10)
    city=models.CharField(default=None,max_length=25)
    Frontview = models.ImageField(upload_to='images/',null=True,blank=True) 
    Backview = models.ImageField(upload_to='images/',null=True,blank=True)
    Interiorview = models.ImageField(upload_to='images/',null=True,blank=True)
    Leftsideview = models.ImageField(upload_to='images/',null=True,blank=True)
    Rightsideview = models.ImageField(upload_to='images/',null=True,blank=True)
    
    

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])

    def __str__(self):
        n=self.brand+" "+self.modelname
        return n

class sellnewcar(models.Model):

    Companyname=models.CharField(default=None,max_length=250)
    Contactnumber=models.CharField(default=None,max_length=10)
    Email=models.EmailField(default=None,max_length=50)
    brand=models.CharField(default=None,max_length=250)
    modelname=models.CharField(default=None,max_length=250)
    variant=models.CharField(default=None,max_length=10)
    fueltype=models.CharField(default=None,max_length=10)
    price=models.CharField(default=None,max_length=10)
    address=models.TextField(default=None,max_length=250)
    city=models.CharField(default=None,max_length=25)
    Frontview = models.ImageField(upload_to='images/',null=True,blank=True) 
    Backview = models.ImageField(upload_to='images/',null=True,blank=True)
    Interiorview = models.ImageField(upload_to='images/',null=True,blank=True)
    Leftsideview = models.ImageField(upload_to='images/',null=True,blank=True)
    Rightsideview = models.ImageField(upload_to='images/',null=True,blank=True)
    

    def get_absolute_url(self):
        return reverse('newdetails', args=[str(self.id)])
    
    def __str__(self):
        n=self.brand+" "+self.modelname
        return n


class finreq(models.Model):
    MARRIED='Married'
    UNMARRIED='Unmarried'
    MS_CHOICES=((MARRIED,'MARRIED'),(UNMARRIED,'UNMARRIED'))
    user_id=models.ForeignKey(Financer,on_delete=models.CASCADE,related_name='financer_id')
    firstname=models.CharField(default=None,max_length=250)
    middlename=models.CharField(default=None,max_length=250)
    lastname=models.CharField(default=None,max_length=250)
    contactnumber=models.CharField(default=None,max_length=10)
    email=models.EmailField(default=None,max_length=50)
    dateofb=models.DateField(default=date.today)
    maritalstatus=models.CharField(max_length=10,choices=MS_CHOICES,default=UNMARRIED,)
    address=models.TextField(max_length=250,default=None)
    city=models.CharField(default=None,max_length=25)
    occupation=models.CharField(default=None,max_length=25)
    grossincome=models.CharField(default=None,max_length=10)
    aadharcard = models.ImageField(upload_to='images/',null=True,blank=True) 
    pancard = models.ImageField(upload_to='images/',null=True,blank=True) 
    bankstatement = models.ImageField(upload_to='images/',null=True,blank=True) 
    passportsizephoto = models.ImageField(upload_to='images/',null=True,blank=True) 
    ITreturn=models.ImageField(upload_to='images/',null=True,blank=True)


    def get_absolute_url(self):
        return reverse('loanreqdetails', args=[str(self.id)])

    def __str__(self):
        n=self.firstname+" "+self.lastname   
        return n

class favv(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    car=models.ForeignKey(sellcar,on_delete=models.CASCADE)

class favvv(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    car=models.ForeignKey(sellnewcar,on_delete=models.CASCADE)


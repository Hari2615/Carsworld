from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Customer,Financer,sellcar,finreq

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    location = forms.CharField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email=self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.location=self.cleaned_data.get('location')
        customer.save()
        return user

class FinancerSignUpForm(UserCreationForm):
    CompanyName=forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    interest_rate = forms.CharField(required=True)
    City = forms.CharField(required=True)
    Address= forms.CharField(required=True)
    logo= forms.ImageField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_financer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.email=self.cleaned_data.get('email')
        user.save()
        financer = Financer.objects.create(user=user)
        financer.phone_number=self.cleaned_data.get('phone_number')
        financer.interest_rate=self.cleaned_data.get('interest_rate')
        financer.Address=self.cleaned_data.get('Address')
        financer.City=self.cleaned_data.get('City')
        financer.logo=self.cleaned_data.get('logo')
        financer.CompanyName=self.cleaned_data.get('CompanyName')
        financer.save()
        return user

class sellcarform(forms.ModelForm):
   

    class Meta:
        model=sellcar
        fields="__all__"
        #exclude=('user',)
        
class finreqform(forms.ModelForm):
   

    class Meta:
        model=finreq
        fields="__all__"
        #exclude=('user_id',)
        
        
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views import generic
from django.views.generic import CreateView,TemplateView
from .form import CustomerSignUpForm, FinancerSignUpForm, sellcarform, finreqform
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail,EmailMessage
from django.db.models import Q
from django.conf import settings
from django.contrib import messages
from django import forms
from .filters import usedcarfilter,newcarfilter

def register(request):
    return render(request, '../templates/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class financer_register(CreateView):
    model = User
    form_class = FinancerSignUpForm
    template_name = '../templates/financer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('fhome')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                if user.is_customer==True:
                    login(request,user)
                    return redirect('/')
               
                elif user.is_financer==True:
                    login(request,user)

                    return redirect('fhome')
                else:
                    login(request,user)
                    return redirect('ahome')

            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'userlogin.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')



def register(request):
    return render(request,'register.html')



def sellcar_view(request,pk):
    context ={} 
    
    # create object of form 
    form = sellcarform(request.POST or None, request.FILES or None) 
    form.fields['user'].widget = forms.HiddenInput()
    form.initial['user'] = pk
      
    # check if form data is valid 
    if form.is_valid(): 
        # save the form data to model 
        

        #form.save(commit=False)
        #form.user_=request.user
        form.save() 
        return redirect('Home')
        
  
    context['form']= form 
    context['pk']= pk
    return render(request, "sellcar.html", context) 

def fhome(request):
    return render(request, 'fhome.html')

def ahome(request):
    return render(request, 'ahome.html')

def develop(request):
    return render(request, 'develop.html')

class buyoldcar(generic.ListView):
    model=sellcar
    
    

class details(generic.DetailView):
    model=sellcar
    
def email(request,pk):
    user = User.objects.filter(id=request.user.id).first()
    seller = sellcar.objects.filter(id=pk).first()
    email = EmailMessage(
            subject='Interested Buyer',
            body='You have an interest buyer named ' +user.first_name + ' for the car '+ seller.brand+ ' ' + seller.modelname + ' you have listed on Carsworld.'+ 'You can contact him on:'+user.phone_number+'. Else you can reply to this email',
            from_email=settings.EMAIL_HOST_USER,
            to=[seller.Email],
            reply_to=[user.email],
        )
    email.send(fail_silently=False)
    messages.info(request,'Mail with your information has been sent successfully to the owner.Please wait for the response.Thankyou')
    return redirect('details',pk=pk)


class buynewcar(generic.ListView):
    model=sellnewcar

class requests(generic.ListView):
    model=finreq
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = finreq.objects.filter(user_id_id=self.request.user.id).all()
        
        return context    
        

class loanreqdetails(generic.DetailView):
    model=finreq

class newdetails(generic.DetailView):
    model=sellnewcar

def newemail(request,pk):
    user = User.objects.filter(id=request.user.id).first()
    seller = sellnewcar.objects.filter(id=pk).first()
    email = EmailMessage(
            subject='Interested Buyer',
            body='You have an interest buyer named ' +user.first_name + ' for the car '+ seller.brand+ ' ' + seller.modelname + ' you have listed on Carsworld.'+ 'You can contact him on:'+user.phone_number+'. Else you can reply to this email',
            from_email=settings.EMAIL_HOST_USER,
            to=[seller.Email],
            reply_to=[user.email],
        
           
        )
    email.send(fail_silently=False)
    messages.info(request,'Mail with your information has been sent successfully to the Company.Please wait for the response.Thankyou')
    return redirect('newdetails',pk=pk)


class fincar(generic.ListView):
    model=Financer


class findetails(generic.DetailView):
    model=Financer

def finreq_view(request,pk):
    context ={} 
  
    # create object of form 
    
    form = finreqform(request.POST or None, request.FILES or None) 
    form.fields['user_id'].widget = forms.HiddenInput()
    form.initial['user_id'] = pk
      
    # check if form data is valid 
    if form.is_valid(): 
        # save the form data to model 
        form.save() 
  
    context['form']= form 
    context['pk']= pk
    return render(request, "finreq.html", context) 

def finemail(request,pk):
    user = User.objects.filter(id=request.user.id).first()
    requester = finreq.objects.filter(id=pk).first()
    email = EmailMessage(
            subject='Loan Approved',
            body='Mr/Mrs ' +requester.firstname + ' your loan has been approved ',
            from_email=settings.EMAIL_HOST_USER,
            to=[requester.email],
            reply_to=[user.email],
        
           
        )
    email.send(fail_silently=False)
    requester.delete()
    return render(request,'fhome.html')

def finremail(request,pk):
    user = User.objects.filter(id=request.user.id).first()
    requester = finreq.objects.filter(id=pk).first()   
    email = EmailMessage(
            subject='Loan Rejected',
            body='Mr/Mrs ' +requester.firstname + ' your loan has been rejected ',
            from_email=settings.EMAIL_HOST_USER,
            to=[requester.email],
            reply_to=[user.email],
        
           
        )
    email.send(fail_silently=False)
    requester.delete()
    return render(request,'fhome.html')


#def search(request): 
#    search=request.GET['search']
 #   sear=sellcar.objects.filter(modelname__icontains=search)
  #  params={'sear':sear}
   # return render(request,'search.html',params)


class SearchResultsView(ListView):
    model = sellcar
    template_name = 'templates/search.html'
    def get_queryset(self): # new
        query = self.request.GET.get('search')
        sear = sellcar.objects.filter(
            Q(modelname__icontains=query) | Q(brand__icontains=query)
        )
        return sear

class SearchResultsnView(ListView):
    model = sellnewcar
    template_name = 'templates/search.html'
    def get_queryset(self): # new
        query = self.request.GET.get('search')
        sear = sellnewcar.objects.filter(
            Q(modelname__icontains=query) | Q(brand__icontains=query)
        )
        return sear


#def nsearch(request): 
 #   search=request.GET['search']
  #  sear=sellnewcar.objects.filter(modelname__icontains=search)
   # params={'sear':sear}
    #return render(request,'nsearch.html',params)

def favview(request,pk):
    
    user = User.objects.filter(id=request.user.id).first()
    ca=sellcar.objects.filter(id=pk).first()
    if favv.objects.filter(car_id=pk).exists():
        favv.objects.filter(car_id=pk).delete()
        messages.info(request,'Removed from favourites')
        return redirect('details',pk=pk)
    else:
       
        favv.objects.create(
            User=user,
            car=ca
        ) 
        messages.info(request,'Added to favourites')     
        return redirect('details',pk=pk)

class favouritel(generic.ListView):
    model=favv
    template_name='accounts/favv_list.html'
    def get_queryset(self):
        return sellcar.objects.filter(id__in=favv.objects.filter(User=self.request.user).values_list('car', flat=True))
        #return favv.objects.filter(User=self.request.user).values_list('car', flat=True)

def favvview(request,pk):
    
    user = User.objects.filter(id=request.user.id).first()
    ca=sellnewcar.objects.filter(id=pk).first()
    if favvv.objects.filter(car_id=pk).exists():
        favvv.objects.filter(car_id=pk).delete()
        messages.info(request,'Removed from favourites')                
        return redirect('newdetails',pk=pk)                         
    else:                                   
     
        favvv.objects.create(               
            User=user,                  
            car=ca
        ) 
        messages.info(request,'Added to favourites')                     
        return redirect('newdetails',pk=pk)                                     

class favvouritel(generic.ListView):
    model=favvv
    template_name='accounts/favvv_list.html'
    def get_queryset(self):
        return sellnewcar.objects.filter(id__in=favvv.objects.filter(User=self.request.user).values_list('car', flat=True))
        #return favv.objects.filter(User=self.request.user).values_list('car', flat=True)


def used_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
    sellcar_list=sellcar.objects.all().exclude(user_id=request.user.id)#.exclude(Email=request.user.email)
    myFilter=usedcarfilter(request.GET,queryset=sellcar_list)
    sellcar_list=myFilter.qs
    # add the dictionary during initialization 
    context={"sellcar_list":sellcar_list, "myFilter":myFilter}
          
    return render(request, "accounts/sellcar_list.html", context) 

def new_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
    sellnewcar_list=sellnewcar.objects.all()
    myFilter=newcarfilter(request.GET,queryset=sellnewcar_list)
    sellnewcar_list=myFilter.qs
    # add the dictionary during initialization 
    context={"sellnewcar_list":sellnewcar_list, "myFilter":myFilter}
          
    return render(request, "accounts/sellnewcar_list.html", context) 
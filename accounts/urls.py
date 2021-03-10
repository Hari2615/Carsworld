from django.contrib import admin
from django.urls import path
from . import views
from accounts.views import details
urlpatterns = [
    path('sellcar',views.sellcar_view,name='sellcar'),
    path('finreq/<int:pk>',views.finreq_view,name='finreq'),
    path('userlogin',views.login_request,name='userlogin'),
    path('customer_register',views.customer_register.as_view(),name='customer_register'),
    path('financer_register',views.financer_register.as_view(),name='financer_register'),
    path('register',views.register,name='register'),
    path('logout',views.logout_view,name='logout'),
    path('fhome', views.fhome,name='fhome'),
    path('develop', views.develop,name='develop'),
    path('ahome', views.ahome,name='ahome'),
    path('requests',views.requests.as_view(),name='requests'),
    path('requests/fhomee',views.fhome,name='fhomee'),
    path('requests/<int:pk>',views.loanreqdetails.as_view(), name='loanreqdetails'),
    path('buynewcar',views.buynewcar.as_view(),name='buynewcar'),
    path('buynewcar/<int:pk>',views.newdetails.as_view(), name='newdetails'),
    path('buyoldcar',views.buyoldcar.as_view(),name='buyoldcar'),
    path('buyoldcar/<int:pk>',views.details.as_view(), name='details'),
    path('fincar',views.fincar.as_view(),name='fincar'),
    path('fincar/<int:pk>',views.findetails.as_view(), name='findetails'),
    path('email/<int:pk>',views.email,name='email'),
    path('newemail/<int:pk>',views.newemail,name='newemail'),
    path('finemail/<int:pk>',views.finemail,name='finemail'),
    path('finremail/<int:pk>',views.finremail,name='finremail'),
    path('search',views.SearchResultsView.as_view(),name='search'),
    path('nsearch',views.SearchResultsnView.as_view(),name='nsearch'),
  
    path('favview/<int:pk>',views.favview,name='favview'),
    path('favouritel',views.favouritel.as_view(),name='favouritel'),
    path('favvview/<int:pk>',views.favvview,name='favvview'),
    path('favvouritel',views.favvouritel.as_view(),name='favvouritel'),

    

   
]

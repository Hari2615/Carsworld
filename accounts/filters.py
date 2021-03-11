import django_filters
from .models import *

class usedcarfilter(django_filters.FilterSet):
    class Meta:
        model=sellcar
        fields = {
                  'price': ['gt', 'lt'],
                  'brand': ['icontains'],
                  'modelname':['icontains']
                 }



class newcarfilter(django_filters.FilterSet):
    class Meta:
        model=sellnewcar
        fields = {
                  'price': ['gt', 'lt'],
                  'brand': ['icontains'],
                  'modelname':['icontains']
                 }
        
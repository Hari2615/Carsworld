import django_filters
from .models import sellcar

class usedcarfilter(django_filters.FilterSet):
    class Meta:
        model=sellcar
        fields = {
                  'price': ['gt', 'lt'],
                  'brand': ['icontains'],
                  'modelname':['icontains']
                 }
        
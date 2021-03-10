from django.contrib import admin
from .models import User, Customer, Financer, sellcar, sellnewcar, finreq

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Financer)
admin.site.register(sellnewcar)
admin.site.register(sellcar)
admin.site.register(finreq)
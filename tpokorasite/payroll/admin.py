from django.contrib import admin
from payroll.models import Customer, Supplier, CustomerBatch
# Register your models here.

admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(CustomerBatch)
from django.shortcuts import render
from payroll.models import Customer

# Create your views here.
def mainSite(request, param):
    #folder = param
    menuLinks = ('customers', 'suppliers')
    customersLinks = ('new', 'order', 'list')
    suplliersLinks = ('new',)
    customers = Customer.objects.all()
    return render(request, 'payroll/index.html', {'menuLinks' : menuLinks,
                                                  'customersLinks' : customersLinks,
                                                  'suppliersLinks' : suplliersLinks,
                                                  'customers' : customers,
                                                  'opt' : param})

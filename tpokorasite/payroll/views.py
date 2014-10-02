from django.shortcuts import render
from payroll.models import Customer, Supplier

# Create your views here.
def home(request):
    menuLinks = ('customers', 'suppliers')
    return render(request, 'payroll/index.html', {'menuLinks' : menuLinks,})

def mainSite(request, param):
    #folder = param
    menuLinks = ('customers', 'suppliers')
    customers = Customer.objects.all()
    suppliers = Supplier.objects.all()
    return render(request, 'payroll/index.html', {'menuLinks' : menuLinks,
                                                  'customers' : customers,
                                                  'suppliers' : suppliers,
                                                  'opt' : param})

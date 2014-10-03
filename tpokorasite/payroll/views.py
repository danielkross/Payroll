from django.shortcuts import render
from django.utils import timezone
from payroll.models import Customer, Supplier, CustomerBatch
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    menuLinks = ('customers', 'suppliers', 'bank')
    return render(request, 'payroll/index.html', {'menuLinks' : menuLinks,})
    
def mainSite(request, param):
    menuLinks = ('customers', 'suppliers')
    customers = Customer.objects.all()
    suppliers = Supplier.objects.all()
    if (param == 'newCustomer'):
        number = request.POST['customerNumber']
        name = request.POST['customerName']
        addNewCustomer(name, number)
        customers = Customer.objects.all()
        return HttpResponseRedirect('customers')
    if (param == 'newSupplier'):
        number = request.POST['supplierNumber']
        name = request.POST['supplierName']
        addNewSupplier(name, number)
        suppliers = Supplier.objects.all()
        return HttpResponseRedirect('suppliers')
    
    return render(request, 'payroll/index.html', {'menuLinks' : menuLinks,
                                                  'customers' : customers,
                                                  'suppliers' : suppliers,
                                                  'opt' : param})


def addNewCustomer(name, number):
    customer = Customer(number=number, name=name, date=timezone.now())
    print 'Acction:'
    print 'Adding customer to database:'
    print 'customer number: ' + customer.number
    print 'customer name: ' + customer.name
    print 'register date: ' + str(customer.date)
    customer.save()
    
def addNewSupplier(name, number):
    supplier = Supplier(number=number, name=name, date=timezone.now())
    print 'Acction:'
    print 'Adding supplier to database:'
    print 'supplier number: ' + supplier.number
    print 'supplier name: ' + supplier.name
    print 'register date: ' + str(supplier.date)
    supplier.save()
    
    
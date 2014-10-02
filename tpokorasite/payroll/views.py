from django.shortcuts import render

# Create your views here.
def mainSite(request, param):
    #folder = param
    menuLinks = ('customers', 'suppliers')
    customersLinks = ('new', 'order', 'list')
    suplliersLinks = ('new',)
    return render(request, 'payroll/index.html', {'menuLinks' : menuLinks,
                                                  'customersLinks' : customersLinks,
                                                  'suppliersLinks' : suplliersLinks,
                                                  'opt' : param})

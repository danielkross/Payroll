from django.shortcuts import render

# Create your views here.
def mainSite(request):
    text = 'text'
    return render(request, 'payroll/index.html', {'text' : text})

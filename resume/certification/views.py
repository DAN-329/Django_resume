from django.shortcuts import render

# Create your views here.
def cet(request):
    return render(request,'cet.html',context={})
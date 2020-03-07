from django.shortcuts import render


# Create your views here.
def home(request):
    name="Daniel Lester Saldanha"
    edu="B Tech in Computer Science Engineering , 2023"
    My_data={'name':name,'edu':edu}
    return render(request,'base.html',context=My_data)


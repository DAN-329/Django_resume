from django.shortcuts import render


def rec(request):
    return render(request,'rec.html',context={})
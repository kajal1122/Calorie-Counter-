from django.shortcuts import render
from .models import CalorieCount
# Create your views here

def myFun(request):
    if request.method == 'GET':
         a = request.GET['food']
         print(a)
         posts = CalorieCount.objects.filter(Food=a)
         return render(request,'page.html', {'post':posts})

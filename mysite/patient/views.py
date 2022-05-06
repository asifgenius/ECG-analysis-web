from datetime import date, datetime
from sqlite3 import Date
from django.shortcuts import render, redirect
from .models import Weight

def weight(request):
    if request.method == "GET":
        data = Weight.objects.all().order_by('-id')
        return render(request, 'weight.html', {"data": data})

    if request.method == "POST":
            
        weight = request.POST.get('weight')
        print("post email",weight)
        Weight.objects.create(amount=weight)
 
        return redirect('/user/weight')
    



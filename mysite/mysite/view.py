from django.shortcuts import render, redirect

def login(request):
    if request.method == "GET":
            
        email = request.GET.get('email')
        print("email",email)
        psw = request.GET.get('psw')
        print("psw",psw)
        return render(request, 'login.html')

    if request.method == "POST":
            
        email = request.POST.get('email')
        print("post email",email)
        psw = request.POST.get('psw')
        print("post psw",psw)
        return redirect('/home')
    

def home(request):
    
    return render(request, 'main.html')
  
def services(request):
    return render(request, 'services.html')
def clients(request):
    return render(request, 'clients.html')
def contact(request):
    return render(request, 'contact.html')
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def aboutus(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contact.html')
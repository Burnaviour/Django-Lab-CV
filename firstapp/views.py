from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'firstapp/index.html')

def about(request):
    return render(request,'firstapp/about.html')

def projectpage(request):
    return render(request,'firstapp/projectpage.html')  
def cvpage(request):
    return render(request,'firstapp/cvpage.html')   
def contact(request):
    return render(request,'firstapp/contact me.html')    


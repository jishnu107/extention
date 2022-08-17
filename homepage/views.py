from django.shortcuts import render

# Create your views here.

def master_page(request):
    return render(request,'homepage/master.html')

def home_page(request):
    return render(request,'homepage/home.html')

def about_page(request):
    return render(request,'homepage/about.html')

def contact_page(request):
    return render(request,'homepage/contact.html')

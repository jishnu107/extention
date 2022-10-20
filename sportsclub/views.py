from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'sportsclub/home.html')


def contact_page(request):
    return render(request,'sportsclub/contact.html')

def players_page(request):
    return render(request,'sportsclub/players.html')
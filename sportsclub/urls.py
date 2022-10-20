from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home_page,name='home'),
    path('contact',views.contact_page,name='contact'),
    path('players',views.players_page,name='players'),


]

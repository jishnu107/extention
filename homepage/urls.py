from django.urls import path
from . import views

urlpatterns = [
    path('master',views.master_page,name='master'),
    path('home',views.home_page,name='home'),
    path('about',views.about_page,name='about'),
    path('contact',views.contact_page,name='contact'),
    
]
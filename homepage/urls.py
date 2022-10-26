from django.urls import path
from . import views

urlpatterns = [
    path('',views.master_page,name='master'),
    path('home',views.home_page,name='home'),
    path('about',views.about_page,name='about'),
    path('contact',views.contact_page,name='contact'),
    path('cart',views.cart_page,name='cart'),
    path('image',views.image_page,name='image'),
    path('baabtra',views.baabtra_page,name='baabtra'),
    path('newpage',views.new_page,name='newpage'),
    path('cssbox',views.cssbox_page,name='cssbox'),
    path('cssrule',views.cssrule_page,name='cssrule'),
    path('grid',views.grid_page,name='grid'),
    path('gridalign',views.gridalign_page,name='gridalign'),
    path('gridwork',views.gridwork_page,name='gridwork'),
    path('modal',views.modal_page,name='modal'),
    path('js',views.js_page,name='js'),
    path('java',views.java_page,name='java'),
    path('function',views.function_page,name='function'),
    path('array',views.array_page,name='array'),
    path('arprob',views.arprob_page,name='arprob'),
    path('dom',views.dom_page,name='dom'),
    path('domjs',views.domjs_page,name='domjs'),
    path('domwk',views.domwk_page,name='domwk'),
    path('jswk',views.jswk_page,name='jswk'),
    path('jswk2',views.jswk2_page,name='jswk2'),
    path('todo',views.todo_page,name='todo'),
    path('domnew',views.domnew_page,name='domnew'),
    path('domnew1',views.domnew1_page,name='domnew1'),














    
]
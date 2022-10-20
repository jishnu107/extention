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

def cart_page(request):
    return render(request,'homepage/cart.html')

def image_page(request):
    return render(request,'homepage/image.html')

def baabtra_page(request):
    return render(request,'homepage/baabtra.html')

def new_page(request):
    return render(request,'homepage/newpage.html')

def cssbox_page(request):
    return render(request,'homepage/cssbox.html')

def cssrule_page(request):
    return render(request,'homepage/cssrule.html')

def grid_page(request):
    return render(request,'homepage/grid.html')

def gridalign_page(request):
    return render(request,'homepage/gridalign.html')

def gridwork_page(request):
    return render(request,'homepage/gridwork.html')

def modal_page(request):
    return render(request,'homepage/modal.html')

def js_page(request):
    return render(request,'homepage/js.html')

def java_page(request):
    return render(request,'homepage/java.html')

def function_page(request):
    return render(request,'homepage/function.html')

def array_page(request):
    return render(request,'homepage/array.html')

def arprob_page(request):
    return render(request,'homepage/arprob.html')

def dom_page(request):
    return render(request,'homepage/dom.html')

def domjs_page(request):
    return render(request,'homepage/domjs.html')

def domwk_page(request):
    return render(request,'homepage/domwk.html')
def jswk_page(request):
    return render(request,'homepage/jswk.html')
def jswk2_page(request):
    return render(request,'homepage/jswk2.html')




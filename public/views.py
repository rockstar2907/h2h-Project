from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/users/menu')
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def subtheme_old(request, id):
    return render(request, 'subtheme_old.html', {'id': id})

def subtheme(request, id):
    return render(request, 'subtheme.html', {'id': id})
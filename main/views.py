from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def login(request):
    return render(request, 'login.html')

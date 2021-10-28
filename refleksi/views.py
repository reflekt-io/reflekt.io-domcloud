from django.shortcuts import render

def index(request):
    response = {}
    return render(request, 'refleksi_index.html', response)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def index(request):
    response = {}
    return render(request, 'refleksi_index.html', response)
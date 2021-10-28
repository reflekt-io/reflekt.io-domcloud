from django.shortcuts import render, redirect
from .models import Kegiatan
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    kegiatan_list = Kegiatan.objects.all()
    response = {'kegiatan': kegiatan_list,
    }
    return render(request, 'refleksi_index.html', response)
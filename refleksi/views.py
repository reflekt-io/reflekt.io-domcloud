from django.shortcuts import render, redirect
from .models import Kegiatan

def index(request):
    kegiatan_list = Kegiatan.objects.all()
    response = {'kegiatan': kegiatan_list,
    }
    return render(request, 'refleksi_index.html', response)
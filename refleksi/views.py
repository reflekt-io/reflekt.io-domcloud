from django.shortcuts import render, redirect
from .models import Kegiatan
from .forms import KegiatanForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    form = KegiatanForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('/refleksi/')

    kegiatan_list = Kegiatan.objects.all()
    response = {'kegiatan': kegiatan_list,
    }
    return render(request, 'refleksi_index.html', response)

@login_required(login_url='/login/')
def form_kegiatan(request):
    form = KegiatanForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('/refleksi/')

    response = {'form': form }
    
    return render(request, 'refleksi_form.html', response)
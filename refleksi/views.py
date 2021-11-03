from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Kegiatan
from .forms import KegiatanForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    if request.user.is_authenticated:
        kegiatan_list = Kegiatan.objects.filter(user=request.user)
        response = {'kegiatan': kegiatan_list, 'user': request.user}
        return render(request, 'refleksi_index.html', response)
    else :
        return render(request, 'refleksi_index.html')

@login_required(login_url='/login/')
def add_kegiatan(request):
    form_kegiatan = KegiatanForm(request.POST or None)

    if request.method == "POST" and form_kegiatan.is_valid():
        form = form_kegiatan.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('/refleksi/')

    response = {'form': form_kegiatan }
    
    return render(request, 'refleksi_form.html', response)

@login_required(login_url='/login/')
def add_deskripsi(request):
    form_kegiatan = KegiatanForm(request.POST or None)

    if request.method == "POST" and form_kegiatan.is_valid():
        form = form_kegiatan.save(commit=False)
        form.user = request.user
        form.save()
        
        kegiatan = Kegiatan.objects.filter(user=request.user).last()
        return JsonResponse({'user': str(request.user), 'nama': kegiatan.nama, 'deskripsi':kegiatan.deskripsi})
    
    return JsonResponse({'nama': "", 'deskripsi':""})
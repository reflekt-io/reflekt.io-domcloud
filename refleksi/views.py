from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Kegiatan
from .forms import KegiatanForm
import json

@login_required(login_url='/login/')
def index(request):
    kegiatan_list = Kegiatan.objects.filter(user=request.user)
    response = {'kegiatan': kegiatan_list, 'user': request.user}
    return render(request, 'refleksi_index.html', response)

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

    if request.method == "GET":
        kegiatan = Kegiatan.objects.filter(user=request.user)
        data = serializers.serialize("json", kegiatan)
        return HttpResponse(data, content_type="application/json")

    if request.method == "POST" and form_kegiatan.is_valid():
        form = form_kegiatan.save(commit=False)
        form.user = request.user
        form.save()
        
        kegiatan = Kegiatan.objects.filter(user=request.user).last()
        return JsonResponse({'user': str(request.user), 'nama': kegiatan.nama, 'deskripsi':kegiatan.deskripsi})
    
    return JsonResponse({'nama': "", 'deskripsi':""})

@csrf_exempt
def add_kegiatan_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nama = data["nama"]
        deskripsi = data["deskripsi"]

        form = Kegiatan(
            user = request.user,
            nama = nama,
            deskripsi = deskripsi
        )
        
        form.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
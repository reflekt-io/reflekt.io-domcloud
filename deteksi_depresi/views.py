from django.shortcuts import render, redirect

from .models import HasilDeteksiDepresi
from .forms import PHQ9Form

def index(request):
    result = None

    if request.method != 'POST':
        form = PHQ9Form()
    else:
        form = PHQ9Form(data=request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            skor = int(form_data['phq_1']) + int(form_data['phq_2']) + int(form_data['phq_3']) + int(form_data['phq_4']) + int( form_data['phq_5']) + int(form_data['phq_6']) + int(form_data['phq_7']) + int(form_data['phq_8']) + int(form_data['phq_9'])

            if skor >= 20:
                result = "Depresi berat"
            elif skor >= 15:
                result = "Depresi sedang"
            elif skor >= 10:
                result = "Depresi ringan"
            elif skor >= 5:
                result = "Gejala depresi ringan"
            else:
                result = "Tidak terdapat gejala depresi"
            
            if request.user.is_authenticated:
                hasil_sebelum = HasilDeteksiDepresi.objects.filter(owner = request.user).first()
                if hasil_sebelum:
                    hasil_sebelum.result = result
                    hasil_sebelum.save()
                else:
                    HasilDeteksiDepresi.objects.create(owner = request.user, result = result)

    if request.user.is_authenticated:
        hasil_deteksi = HasilDeteksiDepresi.objects.filter(owner=request.user).first()
    else:
        hasil_deteksi = HasilDeteksiDepresi(result=result)

    context = {'form': form, 'hasil_deteksi': hasil_deteksi}
    return render(request, 'phq9.html', context)

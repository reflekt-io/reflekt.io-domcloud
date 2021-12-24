import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HasilDeteksiDepresi
from .forms import PHQ9Form

def phq9(request):
    form = PHQ9Form()

    if request.user.is_authenticated:
        hasil_deteksi = HasilDeteksiDepresi.objects.filter(owner=request.user).first()
    else:
        hasil_deteksi = None

    context = {'form': form, 'hasil_deteksi': hasil_deteksi}
    return render(request, 'phq9.html', context)

def get_phq9_json(request):
    if request.method == 'POST':
        form = PHQ9Form(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            skor = int(form_data['phq_1']) + int(form_data['phq_2']) + int(form_data['phq_3']) + int(form_data['phq_4']) + int(
                form_data['phq_5']) + int(form_data['phq_6']) + int(form_data['phq_7']) + int(form_data['phq_8']) + int(form_data['phq_9'])

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
                hasil_deteksi = HasilDeteksiDepresi.objects.filter(owner=request.user).first()
                if hasil_deteksi:
                    hasil_deteksi.result = result
                    hasil_deteksi.save()
                else:
                    hasil_deteksi = HasilDeteksiDepresi(owner=request.user, result=result)
                    hasil_deteksi.save()
            return JsonResponse({'result': result})
        else:
            return JsonResponse({'error': form.errors})
    return redirect('deteksi_depresi:phq9')

@csrf_exempt
def add_result_flutter(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            result = data["result"]
            
            hasil_deteksi = HasilDeteksiDepresi.objects.filter(owner=request.user).first()
            if hasil_deteksi:
                hasil_deteksi.result = result
                hasil_deteksi.save()
            else:
                hasil_deteksi = HasilDeteksiDepresi(owner=request.user, result=result)
                hasil_deteksi.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def fetch_result_flutter(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            hasil_deteksi = HasilDeteksiDepresi.objects.filter(owner=request.user).first()
            if hasil_deteksi:
                return JsonResponse({"result": hasil_deteksi.result, "date": hasil_deteksi.date}, status=200)
        return JsonResponse({"result": "", "date": ""}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
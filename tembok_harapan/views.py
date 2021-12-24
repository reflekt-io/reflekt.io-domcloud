import json
from django.core import serializers
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import response
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from tembok_harapan.forms import harapanForm
from django.contrib.auth.decorators import login_required
from .models import harapan

@login_required(login_url='/login/')
def index(request):
    log_user =  request.user
    list_harapan = harapan.objects.filter(user=log_user)
    return render(request, 'harapan_list.html', {'list_harapan':list_harapan})

@login_required(login_url='/login/')
def add_harapan(request):
    if request.method == 'POST':
        form = harapanForm(request.POST)
        if form.is_valid():
            harapan_form = form.save(commit=False)
            harapan_form.user = request.user
            harapan_form.save()
            return response.HttpResponseRedirect('/tembok-harapan')

    else:
        form = harapanForm()

    
    return render(request, 'harapan_form.html', {'form':form})


@login_required(login_url='/login/')
def json_tembok_harapan(request):
    data_harapan = harapan.objects.filter(user=request.user)
    data = serializers.serialize('json', data_harapan)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_harapan_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
    
        title_flutter = data["title"]
        harapan_flutter = data["harapan"]

        harapan_form = harapan(title = title_flutter, harapan = harapan_flutter, user = request.user)
        harapan_form.save()

        return JsonResponse({"status": "success"}, status=200)
       
    else:
        return JsonResponse({"status": "error"}, status=401)

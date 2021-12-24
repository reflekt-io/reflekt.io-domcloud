import json
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from kutipan_penyemangat.models import Quotes
from kutipan_penyemangat.forms import QuotesForm
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'kutipan_penyemangat_index.html')

@login_required(login_url='/login/')
def add_quotes(request):
    if request.method == 'POST':
        form = QuotesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kutipan_penyemangat:index'))
    else:
        form = QuotesForm()
        response = {'form': form}
        return render(request, 'kutipan_penyemangat_form.html', response) 

@login_required(login_url='/login/')
def json_kutipan_penyemangat(request):
    data = serializers.serialize('json', Quotes.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_kutipan_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
    
        name = data["name"]
        quotes_form = data["quotes_form"]

        kutipan_form = Quotes(name=name, quotes_form = quotes_form)

        kutipan_form.save()

        return JsonResponse({"status": "success"}, status=200)
       
    else:
        return JsonResponse({"status": "error"}, status=401)
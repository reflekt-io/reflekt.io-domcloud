from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from kutipan_penyemangat.models import Quotes
from kutipan_penyemangat.forms import QuotesForm
from django.core import serializers
# Create your views here.
def index(request):
    return render(request, 'kutipan_penyemangat_index.html')

@login_required(login_url='/admin/login/')
def add_quotes(request):
    if request.method == 'POST':
        form = QuotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-kutipan-penyemangat')
    else:
        form = QuotesForm()
        response = {'form': form}
        return render(request, 'kutipan_penyemangat_form.html', response) 

@login_required(login_url='/admin/login/')
def json_kutipan_penyemangat(request):
    data = serializers.serialize('json', Quotes.objects.all())
    return HttpResponse(data, content_type="application/json")
from django.http.response import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from .models import Quotes
from .forms import QuotesForm
from django.contrib.auth.decorators import login_required

def index(request):
    quotes = Quotes.objects.all() 
    response = {'quotes': quotes}
    return render(request, 'kutipan_penyemangat_index.html', response)
def json(request):
    data = serializers.serialize('json', Quotes.objects.all())
    return HttpResponse(data, content_type="application/json")

@login_required(login_url='/admin/login/')
def add_quotes(request):
    if request.method == 'POST':
        form = QuotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuotesForm()
        response = {'form': form}
        return render(request, 'kutipan_penyemangat_form.html', response) 


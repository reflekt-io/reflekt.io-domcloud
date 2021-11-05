from django.http import response
from django.shortcuts import render, redirect
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


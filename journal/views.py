from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse
from journal.models import Journal
from journal.forms import JournalForm
import json

@login_required(login_url='/login/')
def index(request):
    journals = Journal.objects.filter(user=request.user)
    response = {'journals': journals}
    return render(request, 'journal_index.html', response)

@login_required(login_url='/login/')
def add_journal(request):
    context = {}
  
    # create object of form
    form = JournalForm(request.POST or None)

    # check if form data is valid (prevent from SQL injection, too)
    if form.is_valid() and request.method == 'POST':
        # save the form data to the model
        journal_form = form.save(commit=False)
        # print(journal_form.feeling) -> ['antusias', 'gembira', 'semangat', 'bingung']
        # print(request.user) -> nama usernya (contoh: admin)
        journal_form.user = request.user
        journal_form.save()
        # return to index after saving data (POST Redirect)
        return HttpResponseRedirect(reverse('journal:index'))
    
    context['form']= form
    return render(request, "add_journal.html", context)

@login_required(login_url='/login/')
def get_journal_json(request):
    journals = Journal.objects.filter(user=request.user)
    data = serializers.serialize('json', journals)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_journal_flutter(request):
    # request.method SHOULD BE POST (prevent from SQL injection)
    if request.method == 'POST':
        print(request.body)
        # Load data from JSON sent by Flutter app
        data = json.loads(request.body)

        # Parse the data
        # Change string to list for feeling and factor
        feeling = data["feeling"][1:-1].split(', ')
        factor = data["factor"][1:-1].split(', ')
        anxiety_rate = int(data["anxiety_rate"]) # since JSON only accepts String
        summary = data["summary"]

        # create object with data gathered from Flutter form
        journal_form = Journal(
            feeling = feeling,
            factor = factor,
            anxiety_rate = anxiety_rate,
            summary = summary,
            user = request.user
        )
        
        # Save the data to the database
        journal_form.save()

        # return success JSON response to be processed in Flutter
        return JsonResponse({"status": "success"}, status=200)
    # Else, return error JSON response
    else:
        return JsonResponse({"status": "error"}, status=401)
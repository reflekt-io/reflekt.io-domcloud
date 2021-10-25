from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from journal.models import Journal
from journal.forms import JournalForm

@login_required(login_url='/admin/login/')
def index(request):
    journals = Journal.objects.all()
    response = {'journals': journals}
    return render(request, 'journal_index.html', response)

@login_required(login_url='/admin/login/')
def add_journal(request):
    context = {}
  
    # create object of form
    form = JournalForm(request.POST or None)

    # check if form data is valid (prevent from SQL injection, too)
    if form.is_valid() and request.method == 'POST':
        # save the form data to the model
        form.save()
        # return to index after saving data (POST Redirect)
        return HttpResponseRedirect(reverse('journal:index'))
    
    context['form']= form
    return render(request, "add_journal.html", context)
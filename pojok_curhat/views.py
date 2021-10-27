from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Curhatan
from .forms import CurhatForm

# imported login required
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def index(request):
    Curhat = Curhatan.objects.all().values() 
    response = {'Curhat': Curhat}
    return render(request, 'pojok_curhat_index.html', response)

@login_required(login_url='/admin/login/')
def add_curhat(request):
  
    # create object of form
    form = CurhatForm(request.POST or None)
      
    # check if form data is valid
    if (form.is_valid() and request.method == 'POST'):
        # save the form data to model
        form.save()
        # when saved go back to lab-3
        return HttpResponseRedirect('/')
    
    else:
        form = CurhatForm()

    return render(request, 'pojok_curhat_form.html', {'form': form})

@login_required(login_url='/admin/login/')
def curhat_list(request):
    Curhat = Curhatan.objects.all().values()
    response = {'Curhat': Curhat}
    return render(request, 'pojok_curhat_cards.html', response)


def navbar(request):
    return render(request, 'pojok_curhat_navbar.html')
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Curhatan
from .forms import CurhatForm

# imported login required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/admin/login/')
def index(request):
    curhat = Curhatan.objects.all().values() 
    response = {'curhat': curhat}
    return render(request, 'index.html', response)

@login_required(login_url='/admin/login/')
def add_Curhat(request):
  
    # create object of form
    form = CurhatForm(request.POST or None)
      
    # check if form data is valid
    if (form.is_valid() and request.method == 'POST'):
        # save the form data to model
        form.save()
    
    
    else:
        form = CurhatForm()

    return render(request, 'form.html', {'form': form})

def note_list(request):
    curhat = Curhatan.objects.all().values()
    response = {'curhat': curhat}
    return render(request, 'cards.html', response)

def navbar(request):
    return render(request, 'navbar.html')

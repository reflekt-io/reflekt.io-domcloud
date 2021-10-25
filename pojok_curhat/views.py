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
    return render(request, 'index.html', response)

@login_required(login_url='/admin/login/')
<<<<<<< HEAD
def add_Curhat(request):
=======
def add_curhat(request):
>>>>>>> cfee33232115e578018de7a5a6b4f4b0898ee223
  
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

    return render(request, 'form.html', {'form': form})

<<<<<<< HEAD
@login_required(login_url='/admin/login/')
def Curhat_list(request):
=======
def curhat_list(request):
>>>>>>> cfee33232115e578018de7a5a6b4f4b0898ee223
    Curhat = Curhatan.objects.all().values()
    response = {'Curhat': Curhat}
    return render(request, 'cards.html', response)


def navbar(request):
    return render(request, 'navbar.html')
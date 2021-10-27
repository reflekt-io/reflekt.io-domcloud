from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def index(request):
    form = ContactForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/about-us')
        
    context = {'form':form}
    return render(request, 'about_index.html', context)
  

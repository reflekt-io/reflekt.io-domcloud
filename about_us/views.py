from django.shortcuts import render
from django.http.response import JsonResponse
from .forms import ContactForm

# Create your views here.
def index(request):
    if request.method == 'POST' and  request.is_ajax():
        form = ContactForm(request.POST)
        data = {}

        if form.is_valid():
            form.save()
            data['success'] = True
            return JsonResponse(data)
        else:
            data['success'] = False
            return JsonResponse(data)
    else:
        form = ContactForm()
        return render(request, 'about_us_index.html', {'form':form})
  

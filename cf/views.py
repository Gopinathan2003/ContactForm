from django.shortcuts import render
from cf.forms import *
import logging

# Create your views here.
    
def form(request):  
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        value = logging.getLogger("Test")
        if form.is_valid():
            value.debug(f'{form.cleaned_data['name']},{form.cleaned_data['email']},{form.cleaned_data['message']}')
            success_message = "Your Email has been sent!"
            return render(request, 'form.html', {'form':form, 'success_message':success_message})
        else:
            value.debug("Form is not valid")
        return render(request, 'form.html', {'form': form, 'name': name, 'email': email, 'message': message, })
    return render(request, 'form.html')
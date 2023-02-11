from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

#con HttpResponse podemos regresar un texto 
# como string y se puede formatear añadiendo etiquetas

# Create your views here.

def helloworld(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })
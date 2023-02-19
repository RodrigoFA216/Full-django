from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

#con HttpResponse podemos regresar un texto 
# como string y se puede formatear añadiendo etiquetas

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=='GET':
        # print('enviando formulario')
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    elif request.method=='POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if request.POST['password1']==request.POST['password2']:
            #registrar usuario
            try:
                username=request.POST['username']
                password=request.POST['password1']
                user=User.objects.create(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': 'El usuario ya existe'
                    })
        elif request.POST['password1']!=request.POST['password2']:
            return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las contraseñas no coinciden'
                })
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return render(request,'signup.html', {
        #         'form': UserCreationForm
        #     })
        # else:
        #     return render(request,'signup.html', {
        #         'form': UserCreationForm
        #     })
    
def tasks(request):
    return render(request,'tasks.html')
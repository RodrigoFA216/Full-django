from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
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

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form': AuthenticationForm
        })
    elif request.method == 'POST':
        print(request.POST["username"], request.POST["password"])
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)
        print(user)
        if user is None:
            return render(request,'signin.html',{
                'form': AuthenticationForm,
                'error': 'Ususario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('tasks')
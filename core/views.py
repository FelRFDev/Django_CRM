from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages





def submit_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(request,username=username, password=password)
    
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválida, tente novamente!')
            return redirect('login')
    else:
        authentication_form = AuthenticationForm()
        
        return render(request, 'login_page.html', {'authentication_form': authentication_form})


def lougout_user(request):
    logout(request)
    return redirect('login')
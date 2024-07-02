from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages



# Create your views here.
def login_page(request):
    return render(request, template_name='login.html')


def submit_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/index/')
    else:
        messages.error(request, 'Usuário ou senha inválida!')

    return redirect('/login/') 


def lougout_user(request):
    logout(request)
    return redirect('login')
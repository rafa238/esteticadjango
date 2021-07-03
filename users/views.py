from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, "Te has registrado correctamente")
                return redirect('login')

        return render(request, 'register.html', {
            'register_form': register_form,
        })


def loguear(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, "No te has identificado correctamente")

        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('index')

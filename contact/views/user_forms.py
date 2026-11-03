from django.http import request
from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm



def register(request):
    form = RegisterForm()


    messages.info(request, 'Preencha o formulário para se registrar')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('contact:login')
            

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }

    )

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
                request,
                'contact/user_update.html',
                {
                    'form': form,
                }
        
            )

    form = RegisterUpdateForm(request.POST, instance=request.user)

    if not form.is_valid():
        return render(
                request,
                'contact/user_update.html',
                {
                    'form': form,
                }
        
            )

    form.save()
    return redirect('contact:user_update')

def login_view(request):
    messages.info(request, 'Preencha o formulário para fazer login')

    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Login realizado com sucesso!')
            auth.login(request, user)
            return redirect('contact:index')
        messages.error(request, 'Usuário ou senha inválidos.')

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
        }
    )


def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('contact:index')

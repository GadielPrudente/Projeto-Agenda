from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages


def register(request):
    form = RegisterForm()


    messages.info(request, 'Preencha o formulário para se registrar')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('contact:index')
            

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        }

    )
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'First_name',
            'Last_name', 
            'Phone',
            )

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'First_name',
            ValidationError(
                'mensagem de erro',
                code='inválid'
            )
        )

        self.add_error(
            'Last_name',
            ValidationError(
                'mensagem de erro',
                code='inválid'
            )
        )

        return super().clean()

def create(request):
    if request.method == 'POST':

        context = {
            'form': ContactForm(request.POST)
        }

        return render(request, 'contact/create.html', context)

    

    context = {
                'form': ContactForm()
            }
    
    return render(request, 'contact/create.html', context)

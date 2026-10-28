from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    First_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['First_name'].widget.attrs.update({
    #         'class': 'classe-a classe-b',
    #         'placeholder': 'escreva aqui'

    #     })

    class Meta:
        model = models.Contact
        fields = (
            'First_name',
            'Last_name', 
            'Phone',
            'email', 
            'description',
            'category',
            )

    def clean(self):
        # cleaned_data = self.cleaned_data

        # self.add_error(
        #     'First_name',
        #     ValidationError(
        #         'mensagem de erro',
        #         code='inválid'
        #     )
        # )

        # self.add_error(
        #     'Last_name',
        #     ValidationError(
        #         'mensagem de erro',
        #         code='inválid'
        #     )
        # )

        return super().clean()
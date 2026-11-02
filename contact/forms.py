from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'accept': 'image/*'}),)

    class Meta:
        model = models.Contact
        fields = (
            'First_name',
            'Last_name', 
            'Phone',
            'email', 
            'description',
            'category',
            'picture',
            )

    def clean(self):


        return super().clean()
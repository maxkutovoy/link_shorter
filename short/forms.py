from django.forms import ModelForm, TextInput

from .models import Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['full_link']

        widgets = {
            'full_link': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL'
                }
            )
        }
